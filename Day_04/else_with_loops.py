# In this we will see some practice examples using else with python


# Real World Searching Example

students = ["Ali", "Sara", "Ahmad", "Fatima", "Taha"]
search = "Zara"

for student in students:

    if student == search:
        print(f"Found: {student}")
        break

else:
    print(f"{search} is not in the list")