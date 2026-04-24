# ── The most common real-world exception pattern ──────────────────

import json
import os

def load_data(filename):
    """Load JSON data safely with full error handling."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            print(f"✅ Loaded {len(data)} records from {filename}")
            return data

    except FileNotFoundError:
        print(f"⚠️  '{filename}' not found. Starting fresh.")
        return {}

    except json.JSONDecodeError as e:
        print(f"❌ File is corrupted or invalid JSON: {e}")
        return {}

    except PermissionError:
        print(f"❌ No permission to read '{filename}'")
        return {}

def save_data(filename, data):
    """Save JSON data safely."""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
            print(f"✅ Saved successfully to '{filename}'")

    except PermissionError:
        print(f"❌ No permission to write '{filename}'")

    except Exception as e:
        print(f"❌ Unexpected error while saving: {e}")

# ── Usage ─────────────────────────────────────────────────────────
records = load_data("students.json")   # safe even if missing!
records["new_student"] = {"marks": 88}
save_data("students.json", records)    # safe even if fails!