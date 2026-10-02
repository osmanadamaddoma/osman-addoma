import streamlit as st
from PIL import Image

def extract_numbers_from_image(image_file):
    """
    Vision OCR - يقرأ عداد الساعات من صورة
    """
    try:
        # محاولة استخدام EasyOCR لو متوفر
        import easyocr
        reader = easyocr.Reader(['en'])
        result = reader.readtext(image_file, detail=0)
        # ابحث عن أرقام
        import re
        for text in result:
            nums = re.findall(r"\d+\.?\d*", text)
            if nums:
                return float(nums[0])
    except Exception as e:
        st.info("OCR غير مفعل، أدخل الرقم يدويا. (لتفعيله أضف easyocr في requirements)")

    return None

def analyze_image_with_ai(image: Image.Image):
    st.image(image, caption="الصورة المرفوعة للعداد", width=400)
    st.warning("⚠️ الميزة تحتاج تفعيل EasyOCR - حالياً أدخل القراءة يدوياً")
    return None
