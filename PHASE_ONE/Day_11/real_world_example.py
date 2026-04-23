#In this program we will see how file handling works in python through real world example

# ── Student Record System with File Persistence ───────────────────
# Data saves to file — survives program restart!

import json
import os

DATA_FILE = "student_records.json"

def load_records():
    """Load existing records from file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {}           # return empty dict if file doesn't exist


def save_records(records):
    """Save all records to file."""
    with open(DATA_FILE, "w") as file:
        json.dump(records, file, indent=4)


def add_student(name, marks):
    """Add a student and save immediately."""
    records = load_records()
    records[name] = {
        "marks"     : marks,
        "total"     : sum(marks),
        "percentage": round((sum(marks) / (len(marks)*100))*100, 2)
    }
    save_records(records)
    print(f"✅ '{name}' saved to file!")

def show_all_students():
    """Display all saved students."""
    records = load_records()
    if not records:
        print("No records found.")
        return
    print("\n📋 Saved Student Records:")
    print("─" * 40)
    for name, data in records.items():
        print(f"  {name:<15}: {data['percentage']}%")

# ── Run it ───────────────────────────────────────────────────────
add_student("Ali Hassan",  [88, 76, 92, 65, 95])
add_student("Sara Ahmed",  [65, 82, 71, 79, 68])
add_student("Fatima Khan", [95, 98, 100, 88, 97])