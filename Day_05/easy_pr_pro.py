# In this we will see some some easy level practice problems of lists.

# Q1. Create a list of 5 cities in Pakistan. Print:

# First city
#Last city
# All cities in reverse order

city = ["karachi", "lahore", "islamabad", "multan", "pindi"]

print(city[0])
print(city[-1])
print(city[::-1])



# Q2. Given numbers = [5, 3, 8, 1, 9, 2, 7, 4, 6],
# # without using sort(), find the maximum and minimum using loops.

numbers = [5, 3, 8, 1, 9, 2, 7, 4, 6]
max_num = numbers[0]
min_num = numbers[0]
for i in numbers:
    

    if i > max_num:
        max_num = i

    if i < min_num:
        min_num = i

print(max_num)
print(min_num)


# Q3. Without running, what is the output?

data = [10, 20, 30, 40, 50]
print(data[1:4]) # --> 20,30,40
print(data[-2:]) # --> 40, 50
print(data[::2]) # --> 30,40,50