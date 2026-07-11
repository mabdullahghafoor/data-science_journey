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

# ── 2. SELECTION SORT — O(n²) ────────────────────────────────────
def selection_sort(arr):
    """
    Find minimum in unsorted portion,
    place it at beginning.
    """
    arr = arr.copy()
    n   = len(arr)

    for i in range(n):
        min_idx = i     # assume current is minimum

        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j     # found new minimum

        arr[i], arr[min_idx] = arr[min_idx], arr[i]   # swap

    return arr

print(f"Selection   : {selection_sort(marks)}")

# ── 3. INSERTION SORT — O(n²) best for small/nearly sorted ───────
def insertion_sort(arr):
    """
    Build sorted portion one element at a time.
    Like sorting playing cards in hand.
    """
    arr = arr.copy()

    for i in range(1, len(arr)):
        key  = arr[i]       # element to place
        j    = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]    # shift right
            j -= 1

        arr[j + 1] = key    # place in correct position

    return arr

print(f"Insertion   : {insertion_sort(marks)}")

# ── 4. MERGE SORT — O(n log n) fast and efficient ────────────────
def merge_sort(arr):
    """
    Divide array in half, sort each half,
    merge sorted halves back together.
    """
    if len(arr) <= 1:
        return arr
