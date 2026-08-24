# In this program we will create and access list


marks      = [88, 76, 92, 65, 95]
subjects   = ["Math", "English", "Science", "Urdu", "CS"]
mixed      = [1, "Ali", 3.5, True, None]     # mixed types allowed
empty      = []                               # empty list
nested     = [[1, 2], [3, 4], [5, 6]]        # list inside list


# Accessing Items

print(marks[0])
print(marks[-1])
print(marks[-2])

print()

# Slicing List Items

print(marks[1:4]) # --> print from index 1 to 3
print(marks[0:3]) # --> print from index 2 to 2
print(marks[2:]) # --> print from index 2 till end
print(marks[::2]) # --> print every second element of the list
print(marks[::-1]) # --> print every single element from the end of the list (Reverse List)


