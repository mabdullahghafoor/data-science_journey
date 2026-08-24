# In this program we will solve hard level practice problems of Sets

# Q7. Build a Contact Book system:

#Add a contact (name, phone, email)
#Search by name — show full details
#Update phone or email of existing contact
#Delete a contact
#Display all contacts in a formatted table
#Show total contact count
#Handle case when contact not found gracefully

contact = {
    "c1": {"name": "Ali",  "phone_no": 1020, "email": "abc@gmail.com"},
    "c2": {"name": "Sara", "phone_no": 1212, "email": "xyz@gmail.com"},
    "c3": {"name": "Aila", "phone_no": 1551, "email": "mno@gmail.com"}
}

while True:

    print("\n📱 CONTACT BOOK MENU")
    print("1. Search Contact")
    print("2. Update Contact")
    print("3. Delete Contact")
    print("4. Display All Contacts")
    print("5. Total Contacts")
    print("6. Exit")

    choice = int(input("Enter your choice (1-6): "))

    # SEARCH CONTACT
    if choice == 1:

        name = input("Enter name to search: ")
        found = False

        for cid, bio in contact.items():

            if bio["name"].lower() == name.lower():

                print("\nContact Found")
                print("Name :", bio["name"])
                print("Phone:", bio["phone_no"])
                print("Email:", bio["email"])

                found = True
                break

        if not found:
            print("Contact not found")



    # UPDATE CONTACT
    elif choice == 2:

        name = input("Enter name to update: ")
        found = False

        for cid, bio in contact.items():

            if bio["name"].lower() == name.lower():

                print("1. Update Phone Number")
                print("2. Update Email")

                ch = int(input("Enter choice: "))

                if ch == 1:
                    new_phone = int(input("Enter new phone number: "))
                    bio["phone_no"] = new_phone
                    print("Phone number updated")

                elif ch == 2:
                    new_email = input("Enter new email: ")
                    bio["email"] = new_email
                    print("Email updated")

                else:
                    print("Invalid choice")

                found = True
                break

        if not found:
            print("Contact not found")



    # DELETE CONTACT
    elif choice == 3:

        name = input("Enter name to delete: ")
        found = False

        for cid, bio in contact.items():

            if bio["name"].lower() == name.lower():

                del contact[cid]
                print("Contact deleted successfully")

                found = True
                break

        if not found:
            print("Contact not found")



    # DISPLAY ALL CONTACTS
    elif choice == 4:

        print("\n📋 ALL CONTACTS")

        for cid, bio in contact.items():

            print("---------------------")
            print("Name :", bio["name"])
            print("Phone:", bio["phone_no"])
            print("Email:", bio["email"])



    # TOTAL CONTACTS
    elif choice == 5:

        print("Total Contacts:", len(contact))



    # EXIT
    elif choice == 6:

        print("Exiting Contact Book...")
        break


    else:
        print("Invalid choice. Try again.")