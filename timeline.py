from datetime import datetime, timedelta
import plotly.figure_factory as ff

CATEGORY_COLORS = {
    "Medication": "rgb(255, 99, 132)",
    "Meal": "rgb(54, 162, 235)",
    "Exercise": "rgb(75, 192, 192)",
    "Rest": "rgb(255, 206, 86)",
    "Other": "rgb(153, 102, 255)"
}

def parse_time_string(time_str):
    try:
        return datetime.strptime(time_str, "%I:%M %p")
    except Exception:
        return datetime.now().replace(hour=9, minute=0, second=0, microsecond=0)

def parse_to_gantt_data(plan: dict, num_days: int = 5) -> list:
    data = []
    base_date = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)

    meal_time_map = {
        "breakfast": "8:00 AM",
        "lunch": "1:00 PM",
        "dinner": "7:00 PM"
    }

    for day_offset in range(num_days):
        current_date = base_date + timedelta(days=day_offset)

        # Medications
        for med in plan.get("medications", []):
            for t in med.get("time", ["8:00 AM", "4:00 PM"]):
                start = parse_time_string(t).replace(
                    year=current_date.year, month=current_date.month, day=current_date.day
                )
                end = start + timedelta(minutes=15)
                data.append(dict(
                    Task="Medication",
                    Start=start,
                    Finish=end,
                    Resource=f"{med.get('name', 'Medication')} ({med.get('dose', '')})"
                ))

        # Meals
        for meal in plan.get("meals", []):
            meal_label = meal.get("meal", "").lower()
            time_str = meal_time_map.get(meal_label, "12:00 PM")
            start = parse_time_string(time_str).replace(
                year=current_date.year, month=current_date.month, day=current_date.day
            )
            end = start + timedelta(minutes=45)
            suggestions = ", ".join(meal.get("suggestions", [])) or "Meal"
            data.append(dict(
                Task="Meal",
                Start=start,
                Finish=end,
                Resource=suggestions
            ))

        # Exercise
        for ex in plan.get("exercise", []):
            start = current_date.replace(hour=10)
            end = start + timedelta(minutes=30)
            data.append(dict(
                Task="Exercise",
                Start=start,
                Finish=end,
                Resource=f"{ex.get('activity', '')} ({ex.get('frequency', '')})"
            ))

        # Rest
        for r in plan.get("rest", []):
            rest_times = r.get("time", ["9:00 PM"])
            hours = int("".join(filter(str.isdigit, r.get("amount", "8")))) or 8
            for t in rest_times:
                start = parse_time_string(t).replace(
                    year=current_date.year, month=current_date.month, day=current_date.day
                )
                end = start + timedelta(hours=hours)
                data.append(dict(
                    Task="Rest",
                    Start=start,
                    Finish=end,
                    Resource=f"Sleep ({r.get('amount', '')})"
                ))

    return data

def render_timeline_with_interactivity(plan: dict, num_days: int = 5):
    data = parse_to_gantt_data(plan, num_days=num_days)
    colors = {task: CATEGORY_COLORS.get(task, "gray") for task in set(d["Task"] for d in data)}

    # Set fixed timeline range for exactly 5 days
    start_dates = [d["Start"] for d in data]
    min_start = min(start_dates)
    max_end = min_start + timedelta(days=num_days)

    fig = ff.create_gantt(
        data,
        colors=colors,
        index_col="Task",
        show_colorbar=True,
        group_tasks=True,
        showgrid_x=True,
        showgrid_y=True,
        title=f"🗓️ Interactive 5-Day Care Plan Timeline"
    )

    fig.update_layout(
        xaxis=dict(
            range=[min_start, max_end],
            tickformat="%b %d\n%I:%M %p",
            tickangle=-45,
            fixedrange=True  # prevent zooming out to month/year
        ),
        yaxis=dict(fixedrange=True),
        height=600,
        dragmode=False,
        margin=dict(l=20, r=20, t=60, b=40),
        showlegend=True
    )

    return fig
