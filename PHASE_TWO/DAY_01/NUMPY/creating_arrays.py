# The core object is the ndarray (n-dimensional array).

import numpy as np

#From a Python List

a = np.array([1,2,3,4,5])
print(a)
print(type(a))
print()
# 2D-Array

b = np.array([[1,2,3],
              [3,4,5]])
print(b)
print()

#Useful Creation Shortcuts

c = np.zeros((3,4))
print(c)
print()

d = np.ones((3,3))
print(d)
print()

e = np.arange(0,10,2)
