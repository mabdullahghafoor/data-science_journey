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

