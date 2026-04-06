#In this program we will see how to create sets and some auto duplications in it

# ── Creating Sets ───────────────────────────────────────────────
fruits   = {"apple", "banana", "mango", "apple", "banana"}
print(fruits)
# {'mango', 'apple', 'banana'} → duplicates silently removed!
# ⚠️ order may vary — sets are UNORDERED


numbers  = {1, 2, 3, 4, 5}
mixed    = {1, "hello", 3.14, True}

# ⚠️ IMPORTANT — empty set must use set(), NOT {}
empty_wrong  = {}       # ❌ This creates empty DICTIONARY!
empty_right  = set()    # ✅ This creates empty set


# ── Most powerful use: remove duplicates from a list ─────────────
raw_data  = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
clean     = list(set(raw_data))
print(clean)        # [1, 2, 3, 4, 5] — all duplicates gone!


# ── Real world: find unique visitors ────────────────────────────
visitors_log = [
    "Ali", "Sara", "Ali", "Omar",
    "Sara", "Fatima", "Ali", "Omar"
]
unique_visitors = set(visitors_log)
duplicates_removed = len(visitors_log) - len(unique_visitors)

print(f"Total visits    : {len(visitors_log)}")     # 8
print(f"Unique visitors : {len(unique_visitors)}")  # 4
print(f"Duplicates found: {duplicates_removed}")    # 4

