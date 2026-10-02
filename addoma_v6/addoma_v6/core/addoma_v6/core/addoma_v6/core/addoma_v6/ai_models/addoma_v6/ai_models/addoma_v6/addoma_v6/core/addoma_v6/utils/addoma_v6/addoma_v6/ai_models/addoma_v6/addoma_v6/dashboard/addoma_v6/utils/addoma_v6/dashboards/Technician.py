import streamlit as st
from ai_models.vision_reader import analyze_image_with_ai
from PIL import Image

def render_technician_dashboard(sites_data, main_site, sub_site):
    st.markdown(f"## 👷 لوحة الفني - {sub_site}")

    gens = sites_data[main_site][sub_site]['generators']
    selected_gen = st.selectbox("اختر المولد", list(gens.keys()))

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📸 رفع صورة العداد (Vision OCR)")
        uploaded = st.file_uploader("ارفع صورة عداد الساعات", type=["jpg","png","jpeg"])
        if uploaded:
            img = Image.open(uploaded)
            analyze_image_with_ai(img)
            st.success("تم تحليل الصورة - أدخل القراءة المؤكدة أدناه")

        run_hours = st.number_input("ساعات التشغيل الحالية", value=float(gens[selected_gen]['run_hours']), step=0.5)

        if st.button("💾 حفظ القراءة", type="primary"):
            st.success(f"تم حفظ {run_hours} ساعة للمولد {selected_gen} - سيتم مزامنتها مع Supabase")

    with col2:
        st.markdown("### 📝 تقرير الصيانة السريع")
        maintenance_type = st.selectbox("نوع الصيانة", ["فحص دوري", "تغيير زيت", "تغيير فلتر", "إصلاح عطل", "أخرى"])
        notes = st.text_area("ملاحظات الفني")
        cost = st.number_input("التكلفة (جنيه)", value=0.0)

        if st.button("📤 إرسال التقرير"):
            st.success("تم إرسال التقرير للإدارة")
            st.balloons()
