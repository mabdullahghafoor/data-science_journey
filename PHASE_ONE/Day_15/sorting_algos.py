# in this we will see how sorting algos works in python

# ── SORTING ALGORITHMS ────────────────────────────────────────────
# Understanding HOW sorting works makes you a better programmer
# Even though Python has built-in sort()

# ── 1. BUBBLE SORT — O(n²) simplest but slowest ──────────────────
def bubble_sort(arr):
    """
    Compare adjacent elements, swap if wrong order.
    Largest element 'bubbles' to end each pass.
    """
    arr  = arr.copy()   # don't modify original
    n    = len(arr)
