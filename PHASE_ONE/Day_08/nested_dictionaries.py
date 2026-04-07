# In this program we will see some examples regarding nested dictionaries 

# ── Dictionary inside dictionary ─────────────────────────────────
# This is how APIs return data, how JSON looks,
# how MongoDB documents are structured

classroom = {
    "STU001": {
        "name"  : "Ali Hassan",
        "marks" : {"Math": 88, "English": 76, "CS": 95},
        "cgpa"  : 3.87
    },
    "STU002": {
        "name"  : "Sara Ahmed",
        "marks" : {"Math": 65, "English": 82, "CS": 71},
        "cgpa"  : 3.52
    },
    "STU003": {
        "name"  : "Fatima Khan",
        "marks" : {"Math": 95, "English": 98, "CS": 100},
        "cgpa"  : 3.95
    }
}

# ── Accessing nested data ────────────────────────────────────────
print(classroom["STU001"]["name"])           # Ali Hassan
print(classroom["STU001"]["marks"]["CS"])    # 95
print(classroom["STU003"]["cgpa"])           # 3.95