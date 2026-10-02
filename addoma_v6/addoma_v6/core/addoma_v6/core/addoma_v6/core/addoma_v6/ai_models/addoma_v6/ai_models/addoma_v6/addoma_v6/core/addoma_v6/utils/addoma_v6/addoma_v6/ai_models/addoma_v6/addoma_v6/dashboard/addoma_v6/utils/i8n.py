TRANSLATIONS = {
    "ar": {
        "app_name": "نظام أدوما الذكي V6",
        "live": "مباشر",
        "generator": "مولد",
        "remaining": "المتبقي",
        "hour": "ساعة",
        "maintenance_overdue": "متأخر صيانة",
        "executive_dashboard": "لوحة الإدارة التنفيذية",
        "technician_dashboard": "لوحة الفني الميداني"
    },
    "en": {
        "app_name": "Addoma Smart System V6",
        "live": "LIVE",
        "generator": "Generator",
        "remaining": "Remaining",
        "hour": "hour",
        "maintenance_overdue": "Overdue",
        "executive_dashboard": "Executive Dashboard",
        "technician_dashboard": "Technician Dashboard"
    }
}

def t(key, lang="ar"):
    return TRANSLATIONS.get(lang, TRANSLATIONS["ar"]).get(key, key)
