import numpy as np

a = np.array([15, 3, 72, 8, 45, 29])

# The condition creates a boolean array
mask = a > 20
print(mask)
print()

print(a[mask])
print()

