import streamlit as st
import extra_streamlit_components as stx
from core.auth import AuthManager
from core.database import get_all_sites

st.set_page_config(page_title="Addoma V6 Pro", page_icon="🔐", layout="wide")

if "lang" not in st.session_state: st.session_state.lang = "ar"
if "authenticated" not in st.session_state: st.session_state.authenticated = False

TXT = {
 "ar": {"title": "🔐 بوابة تفعيل النظام الموحد V6", "code": "كود التفعيل:", "btn": "تفعيل", "invalid": "❌ كود غير صحيح"},
 "en": {"title": "🔐 Unified System V6", "code": "Activation Code:", "btn": "Activate", "invalid": "❌ Invalid code"}
}[st.session_state.lang]

auth = AuthManager()
cookie_manager = stx.CookieManager()
auth.check_cookie_auto_login(cookie_manager)

if not st.session_state.authenticated:
    st.title(TXT["title"])
    st.sidebar.subheader("🌐 Language")
    lang_sel = st.sidebar.radio("Lang", ["العربية", "English"], index=0 if st.session_state.lang=="ar" else 1)
    st.session_state.lang = "ar" if "العربية" in lang_sel else "en"
    code_input = st.sidebar.text_input(TXT["code"], type="password")
    if st.sidebar.button(TXT["btn"]):
        if auth.validate_code(code_input, cookie_manager):
            st.rerun()
        else:
            st.sidebar.error(TXT["invalid"])
    st.stop()

st.sidebar.success(f"🟢 {st.session_state.get('client_name','')} | {st.session_state.get('plan','')}")
if st.sidebar.button("🚪 تسجيل خروج"):
    auth.logout(cookie_manager)

if "sites_data" not in st.session_state:
    st.session_state.sites_data = get_all_sites()

st.switch_page("pages/1_Predictive_Maintenance.py")
