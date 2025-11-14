def categorize_by_age(age):
    if 0 <= age <= 9:
        return "Child"
    elif 10 <= age <= 18:
        return "Teenager"
    elif 19 <= age <= 64:
        return "Adult"
    elif 65 <= age <= 120:
        return "Golden Age"
    else:
        return f"Invalid Age: {age}"