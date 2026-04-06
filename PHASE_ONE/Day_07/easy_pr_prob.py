# In this program we will solve some easy level practice problems of Sets


# Q1. Create a list with duplicate values:
# Convert to set to remove duplicates.
# Print how many duplicates were removed.

data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
data_set = set(data)
no_of_rem_dup = len(data) - len(data_set)
print(F"No of Removed Duplicates : {no_of_rem_dup}")


# Q2. Without running, what is the output?

s = {1, 2, 3, 2, 1, 4}
print(len(s)) # --> 4
print(3 in s) # --> True
print(5 in s) # --> False