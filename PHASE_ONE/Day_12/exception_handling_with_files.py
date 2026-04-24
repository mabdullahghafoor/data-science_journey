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
