# risk.py

def detect_risks(plan):
    warnings = []

    if not plan.get("exercise"):
        warnings.append("⚠️ No physical activity found in the plan. Light daily movement is important.")

    if len(plan.get("meals", [])) < 3:
        warnings.append("⚠️ Fewer than 3 meals detected. Ensure balanced nutrition.")

    for r in plan.get("rest", []):
        try:
            hours = int("".join(filter(str.isdigit, r.get("amount", ""))))
            if hours < 6:
                warnings.append("⚠️ Less than 6 hours of rest may lead to fatigue or health issues.")
            elif hours > 10:
                warnings.append("⚠️ More than 10 hours of rest could be a sign of underlying issues.")
        except:
            continue

    med_names = [m.get("name", "").lower() for m in plan.get("medications", [])]
    if "aspirin" in med_names and "ibuprofen" in med_names:
        warnings.append("⚠️ Aspirin and Ibuprofen taken together may increase risk of bleeding.")

    return warnings
