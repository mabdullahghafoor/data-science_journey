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
