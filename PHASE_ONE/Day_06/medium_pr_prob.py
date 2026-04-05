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


# Q5. Given this tuple of student records:
# Loop through using tuple unpacking & print each student's result as Pass/Fail.


records = (
    ("Ali",    88),
    ("Sara",   45),
    ("Fatima", 97),
    ("Omar",   32),
)

for name,mark in records:
    
    status = "PASS" if mark >= 50 else "FAIL"

    print(f"Nmae: {name}     Marks: {mark}     {status}")


# Q6. Write a function get_stats(numbers) that takes a list and returns 
# a tuple of (minimum, maximum, average). 
# Then unpack and print the result.

def get_stats(number):
    average = sum(number)/len(number)
    return min(number),max(number),(average)


print(get_stats(number = [3,8,6,1,9,2,7]))

minimum, maximum,avg = get_stats(number = [3,8,6,1,9,2,7])

print(f"Minimum = {minimum}     Maximum = {maximum}     Average = {avg:.2f}")


        
