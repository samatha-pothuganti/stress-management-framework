def get_suggestions(level):
    if level == "High Stress":
        return "🚨 High stress detected! Reduce screen time, sleep properly, and take a break."
    elif level == "Moderate Stress":
        return "⚠️ Maintain balance. Try light exercise and limit phone usage."
    else:
        return "✅ You're doing well. Keep your routine balanced."