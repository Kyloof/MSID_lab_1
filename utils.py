def convert_duration_to_minutes(duration):
    try:
        minutes, seconds = map(int, duration.split(":"))
        return minutes + (seconds / 60)
    except ValueError:
        return None  
