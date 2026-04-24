# In this we will se  how to make Real World Bulletproof Input System

# ── Making any program crash-proof ───────────────────────────────

def get_integer_input(prompt, min_val=None, max_val=None):
    """
    Get a valid integer from user.
    Keeps asking until valid input received.
    """
    while True:
        try:
            value = int(input(prompt))

            if min_val is not None and value < min_val:
                raise ValueError(
                    f"Value must be at least {min_val}"
                )
            if max_val is not None and value > max_val:
                raise ValueError(
                    f"Value must be at most {max_val}"
                )
            return value    # only returns if everything is valid!

        except ValueError as e:
            print(f"  ❌ Invalid: {e}. Please try again.")

def get_float_input(prompt):
    """Get a valid float from user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  ❌ Please enter a valid decimal number.")

# ── Using bulletproof inputs ──────────────────────────────────────
print("📝 Student Registration")
print("─" * 30)
