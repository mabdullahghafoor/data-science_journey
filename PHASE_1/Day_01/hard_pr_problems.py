# In this file we will solve some hard examples for variables and data types

# Q7. Write a program that:
#- Stores a product name, price (float), and quantity (int)
#- Calculates total cost
#- Prints a formatted receipt like:

#Product  : Notebook
#Price    : PKR 150.00
#Quantity : 3
#─────────────────────
#Total    : PKR 450.00


product = input("Enter Your Product Name: ")
price = float(input("Enter Price Of The Product: "))
quantity = float(input("Enter The Quantity Of The Product: "))

print()
print(f"Product  : {product}")
print(f"Price    : {price}")
print(f"Quantity : {quantity}")
print(f"_________________________")
print(f"Total    : PKR {price*quantity}")


