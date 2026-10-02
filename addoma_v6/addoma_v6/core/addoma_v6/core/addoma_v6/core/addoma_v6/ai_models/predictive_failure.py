import pandas as pd
from datetime import datetime

def analyze_failure_risk(run_hours, target_hours, coolant_temp=85, oil_pressure=4.5):
    remaining = target_hours - run_hours
    risk_score = 0
    reasons = []

    # 1. حساب قرب الصيانة
    if remaining <= 0:
        risk_score += 50
        reasons.append(f"تجاوز ساعات الصيانة بـ {abs(remaining):.0f} ساعة")
    elif remaining < 50:
        risk_score += 30
        reasons.append(f"باقي {remaining:.0f} ساعة فقط للصيانة")

    # 2. حرارة عالية
    if coolant_temp > 95:
        risk_score += 25
        reasons.append(f"حرارة تبريد عالية {coolant_temp}°C")

    # 3. ضغط زيت منخفض
    if oil_pressure < 3.5:
        risk_score += 25
        reasons.append(f"ضغط زيت منخفض {oil_pressure} bar")

    # تحديد الحالة
    if risk_score >= 50:
        status = "🔴 خطر عالي - تدخل فوري"
        color = "red"
    elif risk_score >= 25:
        status = "🟡 تنبيه - مراقبة مستمرة"
        color = "orange"
    else:
        status = "🟢 ممتاز - مستقر"
        color = "green"

    return {"risk_score": risk_score, "status": status, "color": color, "reasons": reasons, "remaining": remaining}
