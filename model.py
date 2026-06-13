def predict_stress(sleep, activity, screen_time, mood):
    stress_score = 0

    # Sleep analysis
    if sleep < 6:
        stress_score += 2
    elif sleep < 7:
        stress_score += 1

    # Activity analysis (steps or hours)
    if activity < 1:
        stress_score += 2
    elif activity < 2:
        stress_score += 1

    # Screen time analysis
    if screen_time > 8:
        stress_score += 2
    elif screen_time > 5:
        stress_score += 1

    # Mood analysis
    if mood < 4:
        stress_score += 2
    elif mood < 6:
        stress_score += 1

    # Final result
    if stress_score >= 6:
        return "High Stress"
    elif stress_score >= 3:
        return "Moderate Stress"
    else:
        return "Low Stress"