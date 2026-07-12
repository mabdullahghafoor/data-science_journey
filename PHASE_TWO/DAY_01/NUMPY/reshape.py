import numpy as np

a = np.arange(12)
print(a.shape)
print()

b= a.reshape(3,4)
print(b)
print()

c = a.reshape(4,3)
print(c)
print()

d = a.reshape(2,6)
print(d)
print()

e = a.reshape(6,2)
print(e)
print()

# All valid — as long as rows × columns = 12


# -1 means "figure it out for me"
f = a.reshape(3,-1) # NumPy calculates: 12/3 = 4 columns
print(f)            # (3, 4)
print()

