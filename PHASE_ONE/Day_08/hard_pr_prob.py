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

    