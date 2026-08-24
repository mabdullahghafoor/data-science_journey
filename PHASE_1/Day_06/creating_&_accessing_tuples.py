# In this program we will some some examples to create and access tupes

# ── Creating Tuples ─────────────────────────────────────────────
coordinates  = (24.8607, 67.0011)           # Karachi GPS
rgb_red      = (255, 0, 0)                  # color values
student_info = ("Ali Hassan", 22, "FAST", 3.87)
empty_tuple  = ()                           # empty tuple


# ⚠️ VERY IMPORTANT — single item tuple needs a trailing comma!
wrong  = (42)       # this is just integer 42 — NOT a tuple
correct = (42,)     # THIS is a tuple — notice the comma!
print(type(wrong))   # <class 'int'>
print(type(correct)) # <class 'tuple'>


# ── Accessing — exactly like lists ──────────────────────────────
print(student_info[0])      # Ali Hassan  → first item
print(student_info[-1])     # 3.87        → last item
print(student_info[1:3])    # (22, 'FAST') → slicing works too!