# In this we will se  how to use raise# In this we will se  how to use raise
# In this we will se  how to use raise

# ── You can CREATE and RAISE your own exceptions ──────────────────
# This is how you enforce rules in your functions

def set_age(age):
    """Set student age with validation."""
    if not isinstance(age, int):
        raise TypeError("Age must be an integer!")
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age > 150:
        raise ValueError("Age is unrealistically high!")
    return age

# ── Using it ─────────────────────────────────────────────────────
try:
    print(set_age(22))          # ✅ 22
    print(set_age(-5))          # ❌ ValueError
except ValueError as e:
    print(f"❌ {e}")

try:
    print(set_age("twenty"))    # ❌ TypeError
except TypeError as e:
    print(f"❌ {e}")

# ── Real world: validate marks input ─────────────────────────────
def validate_marks(marks):
    """Validate a list of marks."""
    if not isinstance(marks, list):
        raise TypeError("Marks must be provided as a list!")
