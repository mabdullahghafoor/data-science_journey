# In This Program we will see how a function calling another function

# ── Real world: break big problems into small functions ──────────
# This is how PROFESSIONAL code is structured

def get_grade(percentage):
    """Return grade based on percentage."""
    if percentage >= 90:   return "A+"
    elif percentage >= 80: return "A"
    elif percentage >= 70: return "B"
    elif percentage >= 60: return "C"
    elif percentage >= 50: return "D"
    else:                  return "F"


def get_status(marks_list):
    """Return Pass/Fail based on marks list."""
    all_passed   = all(m >= 40 for m in marks_list)
    percentage   = (sum(marks_list) / (len(marks_list) * 100)) * 100
    return "Pass ✅" if all_passed and percentage >= 50 else "Fail ❌"

def generate_report(name, marks_list):
    """
    Generate complete student report.
    Calls other functions to do specific jobs.
    """
    total      = sum(marks_list)
    percentage = (total / (len(marks_list) * 100)) * 100
    grade      = get_grade(percentage)      # calls get_grade!
    status     = get_status(marks_list)     # calls get_status!

    print(f"\n  Student  : {name}")
    print(f"  Total    : {total}/{len(marks_list)*100}")
    print(f"  Percent  : {percentage:.1f}%")
    print(f"  Grade    : {grade}")
    print(f"  Result   : {status}")

