# In this we will see some some hard level practice problems of lists.


# Q7. Build a shopping cart system using lists:

# Add items (name + price)
# Remove items by name
# View cart
# Calculate total
# Apply 10% discount if total > PKR 2000
# Print formatted receipt


item_name = []
item_price = []

while True:
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))

    item_name.append(name)
    item_price.append(price)

    choice = input("Add another item (Y/N): ").upper()

    if choice == "N":
        break
    elif choice != "Y":
        print("Invalid Choice!")

print("\nCart Items:")
print(item_name)
print(item_price)

discard_item = input("\nEnter item name to remove: ")

if discard_item in item_name:
    index = item_name.index(discard_item)
    item_name.pop(index)
    item_price.pop(index)
else:
    print("Item not found")

total = sum(item_price)

discount = 0
final_price = total

if total > 2000:
    discount = total * 0.10
    final_price = total - discount

print("\nReceipt")
print("------------------------")

for i in range(len(item_name)):
    print(f"{item_name[i]:<10} PKR {item_price[i]:>8}")

print("------------------------")
print(f"Total: PKR {total}")
print(f"Discount: PKR {discount}")
print(f"Final Price: PKR {final_price}")