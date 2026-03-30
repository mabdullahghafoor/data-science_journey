# In ths we will see some examples related to for loops

# loop through range of a number

for i in range(5):
    print(i)

# Range has three form
range(5) # --> it pront 5 number fromm 0 - 4
range(1,6) # --> it prints number from 1 to (6-1)
range(0,10,2) # --> it print number from 0 to (10-1) with the jum of 2 (0,2,4,6,8)
range(10,0-1) # it prints number from 10 to 0 with the subtraction of -1 (10,9,8,7,6,5,4,3,2,1)

print()

# loop through string

name = "Python"
for letter in name:
    print(letter)

print()

# loop through list

subjects = ["Maths", "English", "Urdu", "Pst", "Chemistry"]
for subject in subjects:
    print(subject)