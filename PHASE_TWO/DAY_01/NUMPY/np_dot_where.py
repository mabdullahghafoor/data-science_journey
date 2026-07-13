#Acts like a vectorized if/else.

import numpy as np

a = np.array([10, 25, 8, 40, 15])

# np.where(condition, value_if_true, value_if_false)

result = np.where(a > 20, "hogh", "low")
print(result)
print()

# Common use: replace values conditionally

b = np.where(a > 20, a, 0)
print(b)
print()

print(np.sort(b))
