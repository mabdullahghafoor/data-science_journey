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
