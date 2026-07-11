# in this we will see how hash maps works in  python


# ── Hashmap = Dictionary in Python ───────────────────────────────
# Key → Value mapping with O(1) average lookup time!
# This is WHY dictionaries are so powerful and fast

# ── Key Hashmap Operations ────────────────────────────────────────
#
# Operation           Time     Meaning
# ──────────────────────────────────────
# Get    d[key]       O(1) → instant lookup
# Set    d[key]=val   O(1) → instant insert
# Delete del d[key]   O(1) → instant delete
# Search key in d     O(1) → instant check

# ── Classic Hashmap Problems ──────────────────────────────────────

# PROBLEM 1: Two Sum
# "Find two numbers that add up to target"
def two_sum(nums, target):
    """
    Find indices of two numbers that sum to target.
    Hashmap solution: O(n) — much better than O(n²)!
    """
    seen = {}   # value → index mapping

    for i, num in enumerate(nums):
        complement = target - num   # what do we need?

        if complement in seen:      # have we seen it before?
            return [seen[complement], i]

        seen[num] = i               # store current number

    return []   # no solution found

print(two_sum([2, 7, 11, 15], 9))   # [0, 1] (2+7=9)
print(two_sum([3, 2, 4], 6))        # [1, 2] (2+4=6)

# PROBLEM 2: Frequency Counter
def get_frequency(data):
    """Count how often each item appears — O(n)"""
    freq = {}
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    return freq
