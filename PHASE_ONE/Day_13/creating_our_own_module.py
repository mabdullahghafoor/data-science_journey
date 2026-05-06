# In this we will see how to create our own modules


# ─────────────────────────────────────────────────

# ── Step 2: Import and use in main.py ───────────────────────────

# FILE: main.py
import utils                        # import whole module

marks = [88, 76, 92, 65, 95]
pct   = utils.calculate_percentage(marks)
grade = utils.get_grade(pct)
status = "Pass ✅" if utils.is_passing(marks) else "Fail ❌"

print(f"Percentage: {pct}%")
print(f"Grade     : {grade}")
print(f"Status    : {status}")

# ── Or import specific functions ─────────────────────────────────
from utils import calculate_percentage, get_grade

pct   = calculate_percentage(marks)   # no 'utils.' prefix needed
grade = get_grade(pct)

