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