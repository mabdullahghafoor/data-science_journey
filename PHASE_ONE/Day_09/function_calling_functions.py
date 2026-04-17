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
