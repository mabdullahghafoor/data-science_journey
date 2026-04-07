# In this program we will see some dictionaries methods

profile = {
    "name"  : "Fatima Khan",
    "age"   : 23,
    "city"  : "Karachi",
    "cgpa"  : 3.95,
    "skills": ["Python", "SQL", "ML"]
}

# ── The 3 most important dictionary methods ───────────────────────
print(profile.keys())     # dict_keys(['name','age','city','cgpa','skills'])
print(profile.values())   # dict_values(['Fatima Khan', 23, 'Karachi',...])
print(profile.items())    # dict_items([('name','Fatima Khan'),...])

# ── Looping through dictionary ───────────────────────────────────

# Method 1 — keys only (default)
for key in profile:
    print(key)

# Method 2 — values only
for value in profile.values():
    print(value)


# Method 3 — BOTH key and value (most common in real life)
for key, value in profile.items():
    print(f"  {key:<10} : {value}")