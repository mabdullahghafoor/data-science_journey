
def is_passing(marks, pass_mark=40, pass_percent=50):
    """Check if student has passed all subjects."""
    all_passed = all(m >= pass_mark for m in marks)
    percentage = calculate_percentage(marks)
    return all_passed and percentage >= pass_percent

PI = 3.14159     # module-level constant





