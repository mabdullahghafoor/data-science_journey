# In this program we will see how to create and access dictionaries

# ── Creating a Dictionary ────────────────────────────────────────
student = {
    "name"      : "Ali Hassan",
    "age"       : 22,
    "university": "FAST-NUCES",
    "cgpa"      : 3.87,
    "enrolled"  : True,
    "subjects"  : ["Math", "CS", "Physics"]   # list as a value!
}


# ── Accessing values ─────────────────────────────────────────────
print(student["name"])           # Ali Hassan
print(student["cgpa"])           # 3.87
print(student["subjects"][0])    # Math → index into nested list


# ── The SAFE way: .get() ─────────────────────────────────────────
# Using [] crashes if key doesn't exist
# .get() returns None safely — no crash!

print(student.get("age"))            # 22
print(student.get("grade"))          # None  → key missing, no crash
print(student.get("grade", "N/A"))   # N/A   → custom default value


# ── Check if key exists ───────────────────────────────────────────
print("name" in student)        # True
print("salary" in student)      # False

