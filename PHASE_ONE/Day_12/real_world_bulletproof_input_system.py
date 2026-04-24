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
