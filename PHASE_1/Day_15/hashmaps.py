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

marks = [88, 76, 88, 92, 76, 88, 65, 92, 88]
freq  = get_frequency(marks)
print(freq)     # {88:4, 76:2, 92:2, 65:1}

# PROBLEM 3: Check if two strings are anagrams
def is_anagram(s1, s2):
    """
    Anagram: same characters, different order
    'listen' and 'silent' are anagrams
    """
    if len(s1) != len(s2):
        return False

    count = {}
    for char in s1:
        count[char] = count.get(char, 0) + 1

    for char in s2:
        if char not in count or count[char] == 0:
            return False
        count[char] -= 1

    return True

print(is_anagram("listen", "silent"))   # True
print(is_anagram("hello",  "world"))    # False

# PROBLEM 4: Group students by grade
def group_by_grade(students):
    """Group students using hashmap — O(n)"""
    groups = {}

    for name, marks in students:
        pct   = (marks / 100) * 100
        grade = ("A+" if pct >= 90 else "A" if pct >= 80
                 else "B" if pct >= 70 else "C" if pct >= 60
                 else "D" if pct >= 50 else "F")

        if grade not in groups:
            groups[grade] = []
        groups[grade].append(name)

    return groups

students = [("Ali",88),("Sara",45),("Fatima",97),
            ("Omar",72),("Zara",88),("Bilal",55)]
groups = group_by_grade(students)
for grade, names in sorted(groups.items()):
    print(f"  {grade}: {names}")