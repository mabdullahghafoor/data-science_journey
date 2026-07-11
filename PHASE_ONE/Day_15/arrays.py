# In thia we will see how to use arrays in python

# ── In Python, Arrays = Lists ─────────────────────────────────────
# But understanding array CONCEPTS is critical for DSA

# ── Key Array Operations & Time Complexity ────────────────────────
#
# Operation          Time        Meaning
# ─────────────────────────────────────────────
# Access  arr[i]     O(1)   → instant, no matter size
# Search  x in arr   O(n)   → checks each element
# Insert  append()   O(1)   → fast at end
# Insert  insert(0)  O(n)   → slow at beginning (shifts all)
# Delete  pop()      O(1)   → fast from end
# Delete  pop(0)     O(n)   → slow from front

import array   # built-in array module (typed arrays)

# Python list (most common)
marks = [88, 76, 92, 65, 95, 45, 78]

# ── Common Array Algorithms ───────────────────────────────────────

# 1. LINEAR SEARCH — find an element
def linear_search(arr, target):
    """Search through array one by one — O(n)"""
    for i, value in enumerate(arr):
        if value == target:
            return i        # return index where found
    return -1               # -1 means not found

result = linear_search(marks, 92)
print(f"Found 92 at index: {result}")   # 2

# 2. BINARY SEARCH — faster search (array must be sorted!)
def binary_search(arr, target):
    """Divide and conquer search — O(log n)"""
    left  = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2      # find middle

        if arr[mid] == target:
            return mid                  # found!
        elif arr[mid] < target:
            left = mid + 1              # target is right half
        else:
            right = mid - 1            # target is left half

    return -1   # not found

sorted_marks = sorted(marks)
print(f"Sorted: {sorted_marks}")
result = binary_search(sorted_marks, 92)
print(f"Binary search found 92 at: {result}")

# 3. FIND MAX & MIN without built-ins
def find_max_min(arr):
    """Find max and min manually — O(n)"""
    maximum = arr[0]    # assume first is max
