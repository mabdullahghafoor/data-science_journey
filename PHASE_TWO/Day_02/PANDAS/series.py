print(s.index)    # RangeIndex(start=0, stop=5, step=1)
print(s.dtype)    # int64

# Custom index
s2 = pd.Series([85, 92, 78], index=["Alice", "Bob", "Carol"])
print(s2)
# Alice    85
# Bob      92
# Carol    78

print(s2["Bob"])   # 92
print(s2[s2 > 80]) # Alice 85, Bob 92  ← boolean indexing works here too

# From a dictionary
data = {"Mon": 100, "Tue": 150, "Wed": 130}
s3 = pd.Series(data)
print(s3)
# Mon    100
# Tue    150
# Wed    130