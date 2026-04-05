# In this program we will solve some medium level practice problems of tuples

# Q4. Try to change an item in a tuple. Observe the error message.
# Then write code to: #
# convert to list → change the value → convert back to tuple. 
# #Print the final tuple.

data = (5,3,8,9,1,6,2)
# data[0] = 3
print(data)

# Error : TypeError: 'tuple' object does not support item assignment

data_list = list(data)
data_list[0] = 10
data_tuple = tuple(data_list)
print(data_tuple)