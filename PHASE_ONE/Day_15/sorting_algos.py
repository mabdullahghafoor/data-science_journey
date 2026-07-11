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

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if not swapped:     # already sorted — stop early!
            break

    return arr

marks = [64, 34, 25, 12, 22, 11, 90]
print(f"Original    : {marks}")
print(f"Bubble Sort : {bubble_sort(marks)}")
