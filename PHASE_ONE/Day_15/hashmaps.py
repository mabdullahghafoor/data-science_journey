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
