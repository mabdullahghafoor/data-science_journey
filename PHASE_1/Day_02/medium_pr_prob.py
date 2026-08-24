# In This program we will solve some medium practice problems for operators

# Q4. A shopkeeper gives 15% discount on a PKR 2,500 item. Calculate:

# Discount amount
# Final price
# Print a clean formatted receipt

actual_price = 2500
discount_percentage = 15 
discounted_price = (discount_percentage * actual_price ) / 100
final_price = actual_price - discounted_price


print()
print()
print()
print("╔════════════════════════════════════╗")
print("             🧾 RECEIPT ")
print("╠════════════════════════════════════╣")
print(f"  Actual Price            : {actual_price:.2f}")
print(f"  Discounted Percentage   : {discount_percentage}%")
print(f"  Discounted Price        : {discounted_price:.2f}")
print(f"  Final Price              : {final_price:.2f}")
print("╚════════════════════════════════════╝")
print()
print()
print()


# Q5. Without running, predict True or False:

x = 10
y = 20
z = 10
print(x == z and y > x)     # --> True
print(not (x > y) or z == x)     # --> True
print(x != y and y != z or x == z)     # --> True


# Q6. A student passes only if:
# - Marks >= 50 **AND**
# - Attendance >= 75%

# Write code using logical operators to check if a student passes.

marks = float(input("Enter your marks: "))
attendance = int(input("Enter your attendance in percentage %: "))

print(((marks >= 50) and (attendance >= 75)) and "Pass" or "Fail")

