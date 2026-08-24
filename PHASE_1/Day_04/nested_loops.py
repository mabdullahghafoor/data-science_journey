# In this program we will see some practice examples using nested loops


# Loop inside the loop
# Outer loop run N times
# For each outer iteration, Inner loop run M times
# Total iteration will be N x M times

# Multippliccation table

for i in range(1,4):
    for j in range(1,4):
        print(f"{i} * {j} = {i*j}")
    print("_" * 15)


# Pattern Placing

row = 5
for i in range(1, row+1):
    print("★ " * i)


