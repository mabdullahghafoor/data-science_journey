import numpy as np

a = np.array([4, 7, 13, 2, 9, 7, 5])

print(np.mean(a))
print()

print(np.median(a))
print()

print(np.std(a))
print()


print(np.var(a))
print()

print(np.max(a))
print()

print(np.min(a))
print()

print(np.argmax(a))
print()

print(np.argmin(a))
print()

print(np.sum(a))
print()

print(np.sort(a))
print()


# On 2D arrays, use axis parameter

b = np.array([[1,2,3],
              [4,5,6]])

print(np.sum(b , axis = 0))
print()

print(np.sum(b, axis = 1))
print()
