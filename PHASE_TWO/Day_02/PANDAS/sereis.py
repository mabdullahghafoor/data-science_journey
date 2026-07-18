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

