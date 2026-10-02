import streamlit as st

def get_supabase_client():
    try:
        from supabase import create_client
        return create_client(st.secrets["supabase"]["url"], st.secrets["supabase"]["key"])
    except:
        return None

def get_all_sites():
    # بيانات تجريبية لو ما فيه Supabase - تقدر تغيرها لاحقا
    return {
        "الخرطوم (القائمة الرئيسية)": {
            "الموقع الرئيسي - كافوري (موقع فرعي)": {
                "address": "الخرطوم - كافوري",
                "generators": {
                    "G1": {"model":"Perkins 410 kVA","run_hours":700.0,"target":940.0,"kw":410.0,"load":250.0},
                    "G2": {"model":"Cummins 250 kVA","run_hours":1200.0,"target":1500.0,"kw":250.0,"load":180.0}
                }
            }
        }
    }

def save_generator_data(main_site, sub_site, gen_key, data: dict):
    supabase = get_supabase_client()
    if not supabase: return False
    try:
        import pandas as pd
        supabase.table("generators").upsert({"main_site":main_site,"sub_site":sub_site,"gen_key":gen_key,**data,"updated_at":pd.Timestamp.now().isoformat()}).execute()
        return True
    except:
        return False
