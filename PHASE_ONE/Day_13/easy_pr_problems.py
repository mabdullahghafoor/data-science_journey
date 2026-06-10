# In this we will solve some easy level problems

# Q1. Import the math module and write a program that:

#Calculates square root of 10 numbers
#Finds the ceiling and floor of 5 decimal numbers
#Calculates log base 10 of: 10, 100, 1000


import math

arr = [4,6,8,10,12,14,16,18,20,22]
square_root  = []
for i in arr:
    num = math.sqrt(i) 
    square_root.append(num)

print(square_root)

dec_num = [4.3,2.8,5.5,6.7,5.0]
floor_num = []
ceil_num = []

for i in dec_num:
    f_num = math.floor(i)
    floor_num.append(f_num)
    c_num = math.ceil(i)
    ceil_num.append(c_num)

print(floor_num)
print(ceil_num)

log_num = [10,100,1000]
log10_num = []
for i in log_num:
    l_num = math.log10(i)
    log10_num.append(l_num)

print(log10_num)


#Q2. Using random module:

#Generate 10 random numbers between 1 and 100
#Pick a random student from a list of 8 names
#Simulate rolling two dice (1-6 each) 5 times

