# ═══════════════════════════════════════════════════
# FILE    : utils/validators.py
# PURPOSE : Input validation with exception handling
# USES    : Functions, Exception Handling, Loops
# ═══════════════════════════════════════════════════


def get_input(prompt, min_len=1):
    """Get non-empty string input."""
    while True:
        value = input(prompt).strip()
        if len(value) >= min_len:
            return value
        print(f"  ❌ Input cannot be empty. Try again.")


def get_int(prompt, min_val=None, max_val=None):
    """Get validated integer input — loops until valid."""
    while True:
        try:
            value = int(input(prompt).strip())
            if min_val is not None and value < min_val:
                raise ValueError(f"Must be ≥ {min_val}")
            if max_val is not None and value > max_val:
                raise ValueError(f"Must be ≤ {max_val}")
            return value
        except ValueError as e:
            print(f"  ❌ Invalid: {e}. Try again.")


def get_float(prompt, min_val=None, max_val=None):
    """Get validated float input."""
    while True:
        try:
            value = float(input(prompt).strip())
            if min_val is not None and value < min_val:
                raise ValueError(f"Must be ≥ {min_val}")
            if max_val is not None and value > max_val:
                raise ValueError(f"Must be ≤ {max_val}")
            return value
        except ValueError as e:
            print(f"  ❌ Invalid: {e}. Try again.")


def validate_email(email):
    """Basic email validation."""
    if "@" not in email or "." not in email.split("@")[-1]:
        raise ValueError(f"Invalid email: {email}")
    return email


    """Validate student ID format."""
    if not sid.startswith("STU") or not sid[3:].isdigit():
            "ID must be like 'STU001'"
