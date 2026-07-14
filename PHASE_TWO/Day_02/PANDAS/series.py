import pandas as pd
import numpy as np

# Create from a list
s = pd.Series([10, 20, 30, 40, 50])
print(s)
# 0    10
# 1    20
# 2    30
# 3    40
# 4    50
# dtype: int64

# Left column = index, right column = values
print(s.values)   # [10 20 30 40 50]  ← NumPy array underneath
print(s.index)    # RangeIndex(start=0, stop=5, step=1)
print(s.dtype)    # int64

# Custom index
s2 = pd.Series([85, 92, 78], index=["Alice", "Bob", "Carol"])
print(s2)
