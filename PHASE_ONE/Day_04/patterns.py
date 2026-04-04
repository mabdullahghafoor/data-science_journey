# In this we will try to do some pattern problems

# First Pattern

# *
# * *
# * * * 
# * * * *
# * * * * * 

for i in range (1,6):
    for j in range(1,i+1):
        print("*", end=" ")
    print()


# Second Pattern

# 1
# 2 2
# 3 3 3 
# 4 4 4 4
# 5 5 5 5 5

for i in range (1,6):
    for j in range(1, i+1):
        print(i, end = " ")
    print()


# Third Pattern

# 5
# 5 4
# 5 4 3
# 5 4 3 2
# 5 4 3 2 1

for i in range(1,6): 
    for j in range(1,i+1):
        print(6-j, end=" ")
    print()
