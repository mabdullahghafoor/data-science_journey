# In this program we will some some examples to about tuples unpacking

# ── Unpacking: assign tuple items to variables ──────────────────
student_info = ("Ali Hassan", 22, "FAST-NUCES", 3.87)

# Without unpacking (ugly)
name = student_info[0]
age  = student_info[1]

# With unpacking (clean & Pythonic) ✅
name, age, uni, cgpa = student_info
print(name)     # Ali Hassan
print(cgpa)     # 3.87

# ── Extended unpacking with * ────────────────────────────────────
first, *middle, last = (1, 2, 3, 4, 5)
print(first)    # 1
print(middle)   # [2, 3, 4]
print(last)     # 5

# ── Variable swapping — Python does this via tuples internally ───
a, b = 10, 20
a, b = b, a         # elegant swap — no temp variable needed!
print(a, b)         # 20 10

# ── Functions returning multiple values return tuples ────────────
def get_min_max(data):
    return min(data), max(data)     # returns a tuple!

result = get_min_max([88, 45, 97, 32, 78])
print(result)           # (32, 97)

low, high = get_min_max([88, 45, 97, 32, 78])   # unpacked!
print(f"Low: {low}  High: {high}")
