import numpy as np

a = np.array([10,20,30,40,50])

# Indexing (same as Python lists)

print(a[0])
print(a[-1])
print()

# Slicing: [start:stop:step]

print(a[1:4])
print(a[::2])
print()

# 2D arrays

b = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

print(b[0,1])
print(b[1, :])
print(b[: , 2])
print(b[0:2, 1:3])
print()

#Note: The pattern for 2D: array[row, column].
