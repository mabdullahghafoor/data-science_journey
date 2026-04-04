# In This program we will solve some medium practice problems for operators

# Q4.** Build a **login system**:
# - Stored username: `"admin"`
# - Stored password: `"python123"`
# - Take both as input
# - Print appropriate message for: correct, wrong password only, wrong username


stored_username = "admin"
stored_password = "python123"

username = input("Enter Username: ")
password = input ("Enter Password: ")

if (username == stored_username) and (password == stored_password):
    print("Successfully Logged In!")

else:
    if (username == stored_username) and (password != stored_password):
        print("Invalid Password! Try Again!")
    elif (username != stored_username) and (password == stored_password):
        print("Invalid Username! Try Again!")
    else:
        print("Invalid Credentials. Please Try Again!")


# **Q5.** Write a **traffic light** system:
# - `"Red"` → Stop
# - `"Yellow"` → Slow down
# - `"Green"` → Go
# - anything else → Invalid signal
# Use both `if/elif/else` AND then rewrite with `match`

# Using if/elif/else

color = input("Enter Color Of A Traffic Signal: ").upper()


if (color == "RED"):
    print("STOP!🛑")
elif (color == "YELLOW"):
    print("SLOW DOWN!🟡")
elif (color == "GREEN"):
    print("GO NOW!🟢")
else:
    print("Invalid Signal!🚦")


match color:

    case "RED":
        print("STOP!🛑")
    case "YELLOW":
        print("SLOW DOWN!🟡")
    case "GREEN":
        print("GO NOW!🟢")
    case _: 
        print("Invalid Signal!🚦")



# **Q6.** A shopping site gives discounts:
# - Purchase >= PKR 5000 AND member → 20% off
# - Purchase >= PKR 5000 but not member → 10% off
# - Purchase < PKR 5000 AND member → 5% off
# - Otherwise → No discount

# Write the logic and print the final price.

purchase = int(input("Enter Total Purchase Amount: "))
member = input("Are You A Member (Y/N): ").upper()

# Step 1: Decide discount %
n = 0

if purchase >= 5000 and member == "Y":
    n = 20
elif purchase >= 5000 and member == "N":
    n = 10
elif purchase < 5000 and member == "Y":
    n = 5

# Step 2: Calculate once
discount = (purchase * n) / 100
final_amount = purchase - discount

# Step 3: Print once
print("\n ----------- BILL RECEIPT -----------")
print(f"Purchasing Amount = PKR {purchase}/-")
print(f"Discount Percentage = {n}%")
print(f"Discount Amount = PKR {discount}/-")
print("-------------------------------------")
print(f"Final Amount = PKR {final_amount}/-")