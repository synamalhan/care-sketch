def format_plan_for_display(plan: dict) -> str:
    display = ""

    # Medications
    meds = plan.get("medications", [])
    if meds:
        display += "### 💊 Medications\n"
        for med in meds:
            name = med.get("name", "Unknown")
            dose = med.get("dose", "No dosage info")
            times = ", ".join(med.get("time", [])) or "No time specified"
            display += f"- **{name}**: {dose} at {times}\n"
        display += "_Note: It's best to consult a doctor before taking any medication._\n\n"

    # Meals
    meals = plan.get("meals", [])
    if meals:
        display += "### 🍽️ Meals\n"
        for meal in meals:
            meal_time = meal.get("meal", "Unknown")
            suggestions = meal.get("suggestions", [])
            display += f"- **{meal_time.capitalize()}**:\n"
            for food in suggestions:
                display += f"  - {food}\n"
        display += "\n"

    # Exercise
    exercises = plan.get("exercise", [])
    if exercises:
        display += "### 🏃 Exercise\n"
        for ex in exercises:
            activity = ex.get("activity", "Unknown activity")
            duration = ex.get("duration", "Unknown duration")
            frequency = ex.get("frequency", "Unknown frequency")
            display += f"- **{activity}** for {duration}, {frequency}\n"
        display += "\n"

    # Rest
    rests = plan.get("rest", [])
    if rests:
        display += "### 😴 Rest\n"
        for r in rests:
            amount = r.get("amount", "Unknown amount")
            times = ", ".join(r.get("time", [])) or "Unknown time"
            display += f"- Sleep for {amount} during {times}\n"
        display += "\n"

    # Notes
    notes = plan.get("notes", [])
    if notes:
        display += "### 📝 Notes\n"
        for note in notes:
            display += f"- {note}\n"
        display += "\n"

    if not display.strip():
        display = "_No plan data available._"

    return display
