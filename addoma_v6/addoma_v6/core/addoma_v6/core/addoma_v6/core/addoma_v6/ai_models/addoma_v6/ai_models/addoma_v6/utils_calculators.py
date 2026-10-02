def calculate_cost_per_kwh(fuel_liters, fuel_price_sdg, kwh_produced):
    if kwh_produced <= 0: return 0
    return (fuel_liters * fuel_price_sdg) / kwh_produced

def calculate_sbc601_compliance(wall_thickness_mm, insulation_type="polyurethane"):
    # حساب بسيط لمطابقة كود العزل السعودي SBC 601
    k_values = {"polyurethane": 0.024, "polystyrene": 0.035, "rockwool": 0.040}
    k = k_values.get(insulation_type, 0.024)
    u_value = k / (wall_thickness_mm / 1000.0)  # W/m2.K
    compliant = u_value <= 0.3  # حد SBC 601 للتبريد
    return {"u_value": round(u_value,4), "compliant": compliant, "required_thickness": round((k/0.3)*1000,1)}

def energy_efficiency_score(load_kw, rated_kw):
    if rated_kw == 0: return 0
    load_factor = (load_kw / rated_kw) * 100
    if 70 <= load_factor <= 85: score = 100
    elif 50 <= load_factor < 70: score = 80
    elif load_factor < 50: score = 60
    else: score = 70
    return {"load_factor": round(load_factor,1), "score": score}
