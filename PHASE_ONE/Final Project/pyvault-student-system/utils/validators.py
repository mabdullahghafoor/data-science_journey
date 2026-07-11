# ═══════════════════════════════════════════════════
def get_float(prompt, min_val=None, max_val=None):
    while True:
            value = float(input(prompt).strip())
            if min_val is not None and value < min_val:
            if max_val is not None and value > max_val:
            return value
            print(f"  ❌ Invalid: {e}. Try again.")
def validate_email(email):
        raise ValueError(f"Invalid email: {email}")

