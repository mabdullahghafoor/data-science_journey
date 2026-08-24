import numpy as np

a = np.array([[1,2,3],
              [4,5,6]])

print(a.shape)
print(a.ndim)
print(a.dtype)
print(a.size)
print()

# dtype matters — NumPy arrays are homogeneous (one type only)

c = np.array([1,2,3.5]) # one float forces ALL elements to float
print(c.dtype)
print(c)
print()


# You can specify dtype explicitly

d =np.array([1,2,3], dtype = float)
print(d)
print()