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

