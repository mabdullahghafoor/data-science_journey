# In this we will some some medium level practice problems for variables and data types

# Q4. Ask yourself: a user enters their age as "23" (string). Write code that:

# Converts it to int
# Adds 10 to it
# Prints: "In 10 years, you will be 33 years old."

age = input("Enter your age: ")
num = int(age)
print(f"In 10 years, you will be {num+10} years old.")


# Q5. Given the string "data_science_2024", extract just the word "science" using slicing.

msg = "data_science_2024"
print(msg[5:12])

# Q6. Without running it first, predict the output:

a = 5.0
b = 2
c = a // b
print(type(c))
