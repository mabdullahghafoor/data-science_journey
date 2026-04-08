# In This program we will solve some easy level practice problems

# Q1. Create a dictionary for yourself with these keys: 
# name, age, city, favourite_language, is_student. Print every key-value pair using a loop.

bio = {
    "name" : "Abdullah",
    "age"  : 21,
    "city" : "Karachi",
    "favourite_language" : "Pyhton",
    "is_student" : True
}

for att, val in bio.items():
    print(f"{att:>15} : {val:>15}")


# Q2. Without running, what is the output?

d = {"a": 1, "b": 2, "c": 3}
print(d.get("b")) # --> 2
print(d.get("z", "Not Found")) # --> Not Found
print("c" in d) # --> True
print(len(d)) # --> 3


# Q3. Given this dictionary:
# Print the most expensive and cheapest fruit with their prices.

prices = {"apple": 150, "banana": 80, "mango": 200, "grape": 350}
