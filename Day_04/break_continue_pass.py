# In this program we will solve some examples related to break continue and pass 

# Break: Exit the loop completely

for i in range(10):
    if i == 5:
        break
    print(i)  # --> it print number until 5 comes and does.nt print 5


# Continue: Skips Current iteration keep looping

for i in range(10):
    if i % 2 == 0:
        continue
    print(i) # --> It prints all odd numbers skips the even


# Pass: Do Nothing 

for i in range(10):
    if i == 3:
        pass
    print(i) # --> It prints all numbers do nothing when i = 3s