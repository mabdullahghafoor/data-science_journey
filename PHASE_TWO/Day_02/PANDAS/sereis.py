#A Series is a one-dimensional labeled array. 
# One column of data with an index.

import pandas as pd

import numpy as np

s = pd.Series([10,20,30,40,50])

print(s)
print()

#0    10
#1    20
#2    30
#3    40
#4    50
#dtype: int64

print(s.values)
print()

print(s.index)
print()

print(s.dtype)
print()

# Custom index

s2 = pd.Series([85,92,78] , index=["Alice", "Bob", "Carol"])

print(s2)
print()

print(s2["Bob"])
print()

print(s2[s2 > 80])
print()


# From a dictionary

data = {"Mon" : 100 , "Tue" : 150 , "Wed" : 200}
