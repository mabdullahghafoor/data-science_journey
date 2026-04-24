# In this we will se  how to use multiple exceptions

# ── Method 1: Separate except blocks ─────────────────────────────
def safe_divide(a, b):
    """Safely divide two numbers with full error handling."""
    try:
        result = a / b
        return result