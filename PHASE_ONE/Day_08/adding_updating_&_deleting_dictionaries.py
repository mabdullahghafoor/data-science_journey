# In this program we will see how to update , add and deleyte values in dictioonaries

student = {"name": "Ali", "cgpa": 3.5}

# ── Add new key-value pair ───────────────────────────────────────
student["university"] = "FAST"
student["age"]        = 22
print(student)
# {'name':'Ali', 'cgpa':3.5, 'university':'FAST', 'age':22}


# ── Update existing value ────────────────────────────────────────
student["cgpa"] = 3.87          # simply reassign
print(student["cgpa"])          # 3.87


# ── Update multiple keys at once ─────────────────────────────────
student.update({"age": 23, "cgpa": 3.90, "city": "Karachi"})
print(student)


# ── Deleting ─────────────────────────────────────────────────────
del student["age"]                       # delete specific key
removed = student.pop("university")      # delete AND return value
print(f"Removed: {removed}")             # FAST


last = student.popitem()                 # removes LAST inserted pair
print(f"Last item removed: {last}")      # ('city', 'Karachi')