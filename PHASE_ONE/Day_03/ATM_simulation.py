# ─────────────────────── ATM Simulation ─────────────────────
# Demonstrates: nested conditions + logical operators + real logic

stored_pin = 1234
balance = 50000

print("\n------------ Welcome to XYZ ATM ------------")

pin = int(input("\nEnter your 4-digit PIN: "))

if (pin == stored_pin):
    print("\nWelcome!")

    print("\nChooose Option: ")
    print("1. Cash Withdraw")
    print("2. Check Balance")
    print("3. Exit")

    choice = input("\nEnter your Choice(1-3): ")

    if (choice == "1"):
        amount = int(input("\nEnter Amount: "))

        if (amount <= 0):
            print("\nPlease Enter amount Greater Than Zero(0)")
        if (amount > balance):
            print("\nInsufficient Balnce")
        if (amount % 500 != 0):
            print("\nAmount should be multiple of 500")

        else:
            balance -= amount
            print(f"\n✅ PKR{amount}, dispensed")
            print(f"Your remaining balnce = {balance}")

    elif (choice == "2"):
        print(f"\nBalnce = {balance}")


    elif (choice == "3"):
        print("\nThank You, Have a Good Day!")


    else:
        print("\n❌ Invalid Choice!")


else:
    print("\n❌ Invalid PIN. Please Try Again!")