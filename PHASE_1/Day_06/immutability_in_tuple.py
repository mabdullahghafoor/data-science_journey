# In this program we will some some examples to about immutability tuples

# ── Tuples CANNOT be changed ────────────────────────────────────
coordinates = (24.8607, 67.0011)

# Try to change → Python will crash with error
coordinates[0] = 25.0
# ❌ TypeError: 'tuple' object does not support item assignment

# ── But here is a trick — convert when needed ───────────────────
coords_list = list(coordinates)     # tuple → list
coords_list[0] = 25.0               # change it
coordinates = tuple(coords_list)    # list → tuple again
print(coordinates)                  # (25.0, 67.0011)