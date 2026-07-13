import numpy as np

a = np.array([1,2,3,4,5])
b = np.array([10,20,30,40,50])

print(a + b)
print()
print(a * b)
print()
print(a ** 2)
print()
print(a + 100)
print()


# These are all vectorized — no for loop needed
# Compare with plain Python:
# result = [a[i] + b[i] for i in range(len(a))]  ← slow
# np gives you the same result instantly at any scale