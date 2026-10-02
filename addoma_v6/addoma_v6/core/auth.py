import streamlit as st
from datetime import datetime, timedelta

class AuthManager:
    def __init__(self):
        try:
            from supabase import create_client
            self.supabase = create_client(st.secrets["supabase"]["url"], st.secrets["supabase"]["key"])
        except:
            self.supabase = None

    def validate_code(self, code, cookie_manager):
        # وضع تجريبي لو ما فيه Supabase
        if not self.supabase:
            if code.strip().upper() in ["DEMO","ADMIN","ADDOMA2025"]:
                st.session_state.authenticated=True
                st.session_state.client_name="Demo Client"
                st.session_state.plan="Pro Annual"
                return True
            return False
        try:
            res = self.supabase.table("subscriptions").select("*").eq("code", code.strip().upper()).execute()
            if not res.data: return False
            row = res.data[0]
            start = datetime.strptime(row["start_date"], "%Y-%m-%d")
            if datetime.now() > start + timedelta(days=row["duration_days"]):
                st.error("انتهى الاشتراك"); return False
            st.session_state.authenticated = True
            st.session_state.client_name = row["client_name"]
            st.session_state.plan = row["plan"]
            try: cookie_manager.set("activation_code_v6", code, expires_at=datetime.now()+timedelta(days=30))
            except: pass
            st.query_params["code"] = code
            return True
        except Exception as e:
            st.error(f"Auth Error: {e}"); return False

    def check_cookie_auto_login(self, cookie_manager):
        try:
            saved = cookie_manager.get("activation_code_v6")
            if saved and not st.session_state.authenticated:
                self.validate_code(saved, cookie_manager)
        except: pass

    def logout(self, cookie_manager):
        try: cookie_manager.delete("activation_code_v6")
        except: pass
        st.session_state.clear()
        st.rerun()
