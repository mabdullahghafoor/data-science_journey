# In this we will see how we can create our own modules


# ── Step 1: Create utils.py ──────────────────────────────────────

# FILE: utils.py
# ─────────────────────────────────────────────────
"""
utils.py — Reusable utility functions
for the Student Management System.
"""

def calculate_percentage(marks, total_per_subject=100):
    """Calculate percentage from a list of marks."""
    total    = sum(marks)
    max_total = len(marks) * total_per_subject
    return round((total / max_total) * 100, 2)

