def get_grade(percentage):
    """Return grade based on percentage."""
    if   percentage >= 90: return "A+"
    elif percentage >= 80: return "A"
    elif percentage >= 70: return "B"
    elif percentage >= 60: return "C"
    elif percentage >= 50: return "D"
    else:                  return "F"

def is_passing(marks, pass_mark=40, pass_percent=50):
    """Check if student has passed all subjects."""
    all_passed = all(m >= pass_mark for m in marks)
    percentage = calculate_percentage(marks)
    return all_passed and percentage >= pass_percent

PI = 3.14159     # module-level constant





