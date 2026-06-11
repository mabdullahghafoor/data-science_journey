# ═══════════════════════════════════════════════════════════════
# PROJECT  : Smart Contact Vault
# PURPOSE  : Command-line contact management system
# CONCEPTS : Dictionaries, Lists, Tuples, Sets
# AUTHOR   : Your Name
# ═══════════════════════════════════════════════════════════════


# ── CONTACT DATABASE ────────────────────────────────────────────
# Main store: dictionary of dictionaries
# Key = contact ID, Value = contact details dict

contacts = {
    "C001": {
        "name" : "Ali Hassan",
        "phone": "0312-1234567",
        "email": "ali@email.com",
        "city" : "Karachi"
    },
    "C002": {
        "name" : "Sara Ahmed",
        "phone": "0321-9876543",
        "email": "sara@email.com",
        "city" : "Lahore"
    },
    "C003": {
        "name" : "Fatima Khan",
        "phone": "0333-5556677",
        "email": "fatima@email.com",
        "city" : "Islamabad"
    },
    "C004": {
        "name" : "Omar Farooq",
        "phone": "0345-1112233",
        "email": "omar@email.com",
        "city" : "Karachi"
    },
    "C005": {
        "name" : "Zara Malik",
        "phone": "0311-7778899",
        "email": "zara@email.com",
        "city" : "Lahore"
    },
}

# ── COUNTER for generating new contact IDs ───────────────────────
contact_counter = len(contacts) + 1


# ════════════════════════════════════════════
#   HELPER FUNCTIONS
# ════════════════════════════════════════════

def print_line():
    """Print a separator line."""
    print("─" * 55)

def print_header(title):
    """Print a formatted section header."""
    print()
    print("╔" + "═" * 53 + "╗")
    print(f"  {title}")
    print("╚" + "═" * 53 + "╝")

def generate_id():
    """Generate a new unique contact ID."""
    global contact_counter
    new_id = f"C{contact_counter:03d}"
    contact_counter += 1
    return new_id

def get_all_cities():
    """Return a SET of all unique cities — no duplicates."""
    return {data["city"] for data in contacts.values()}

def get_contact_snapshot(contact_id):
    """Return contact as an immutable TUPLE record."""
    if contact_id in contacts:
        c = contacts[contact_id]
        return (contact_id, c["name"], c["phone"],
                c["email"], c["city"])
    return None


# ════════════════════════════════════════════
#   FEATURE 1 — View All Contacts
# ════════════════════════════════════════════

def view_all_contacts():
    """Display all contacts in a formatted table."""
    print_header("📋 ALL CONTACTS")

    if not contacts:
        print("  No contacts found.")
        return

    print(f"  {'ID':<6} {'Name':<18} {'Phone':<16} {'City':<12}")
    print_line()

    for cid, data in contacts.items():
        print(f"  {cid:<6} {data['name']:<18} "
              f"{data['phone']:<16} {data['city']:<12}")

    print_line()
    print(f"  Total Contacts: {len(contacts)}")


# ════════════════════════════════════════════
#   FEATURE 2 — Add Contact
# ════════════════════════════════════════════

def add_contact():
    """Add a new contact to the vault."""
    print_header("➕ ADD NEW CONTACT")

    name  = input("  Enter name  : ").strip()
    phone = input("  Enter phone : ").strip()
    email = input("  Enter email : ").strip()
    city  = input("  Enter city  : ").strip()

    # Validate — name and phone are required
    if not name or not phone:
        print("\n  ❌ Name and phone are required!")
        return

    # Check for duplicate phone number
    for data in contacts.values():
        if data["phone"] == phone:
            print(f"\n  ⚠️  Phone already exists for: {data['name']}")
            return

    # Generate ID and store
    new_id = generate_id()
    contacts[new_id] = {
        "name" : name,
        "phone": phone,
        "email": email,
        "city" : city
    }

    print(f"\n  ✅ Contact added! ID: {new_id}")


# ════════════════════════════════════════════
#   FEATURE 3 — Search Contact
# ════════════════════════════════════════════

def search_contact():
    """Search for a contact by name (partial match)."""
    print_header("🔍 SEARCH CONTACT")

    query   = input("  Enter name to search: ").strip().lower()
    results = []

    # Search through all contacts
    for cid, data in contacts.items():
        if query in data["name"].lower():   # partial match!
            results.append((cid, data))

    if not results:
        print(f"\n  ❌ No contacts found for '{query}'")
        return

    print(f"\n  Found {len(results)} result(s):\n")
    for cid, data in results:
        print(f"  ID     : {cid}")
        print(f"  Name   : {data['name']}")
        print(f"  Phone  : {data['phone']}")
        print(f"  Email  : {data['email']}")
        print(f"  City   : {data['city']}")
        print_line()


# ════════════════════════════════════════════
#   FEATURE 4 — Update Contact
# ════════════════════════════════════════════

def update_contact():
    """Update details of an existing contact."""
    print_header("✏️  UPDATE CONTACT")

    cid = input("  Enter Contact ID to update (e.g. C001): ").strip()

    if cid not in contacts:
        print(f"\n  ❌ Contact '{cid}' not found!")
        return

    contact = contacts[cid]
    print(f"\n  Updating: {contact['name']}")
    print("  (Press Enter to keep current value)\n")

    # Only update if user provides new value
    new_phone = input(f"  Phone [{contact['phone']}]: ").strip()
    new_email = input(f"  Email [{contact['email']}]: ").strip()
    new_city  = input(f"  City  [{contact['city']}] : ").strip()

    if new_phone: contacts[cid]["phone"] = new_phone
    if new_email: contacts[cid]["email"] = new_email
    if new_city:  contacts[cid]["city"]  = new_city

    print(f"\n  ✅ Contact '{contact['name']}' updated!")


# ════════════════════════════════════════════
#   FEATURE 5 — Delete Contact
# ════════════════════════════════════════════

def delete_contact():
    """Delete a contact by ID."""
    print_header("🗑️  DELETE CONTACT")

    cid = input("  Enter Contact ID to delete (e.g. C001): ").strip()

    if cid not in contacts:
        print(f"\n  ❌ Contact '{cid}' not found!")
        return

    name    = contacts[cid]["name"]
    confirm = input(f"\n  Delete '{name}'? (yes/no): ").strip().lower()

    if confirm == "yes":
        deleted = contacts.pop(cid)     # removes & returns
        print(f"\n  ✅ '{deleted['name']}' deleted successfully!")
    else:
        print("\n  ❌ Deletion cancelled.")


# ════════════════════════════════════════════
#   FEATURE 6 — Browse by City (Uses SETS)
# ════════════════════════════════════════════

def browse_by_city():
    """Show all unique cities and filter contacts by city."""
    print_header("🏙️  BROWSE BY CITY")

    # Use SET to get unique cities — no duplicates!
    unique_cities = get_all_cities()
    city_list     = sorted(unique_cities)   # sorted for display

    print("  Available Cities:")
    for i, city in enumerate(city_list, start=1):
        print(f"    {i}. {city}")

    chosen = input("\n  Enter city name: ").strip().title()

    # Filter contacts by chosen city
    found = {
        cid: data
        for cid, data in contacts.items()
        if data["city"] == chosen
    }

    if not found:
        print(f"\n  ❌ No contacts in '{chosen}'")
        return

    print(f"\n  📍 Contacts in {chosen}:\n")
    for cid, data in found.items():
        print(f"  [{cid}] {data['name']:<18} | {data['phone']}")


# ════════════════════════════════════════════
#   FEATURE 7 — Stats & Summary (Uses TUPLE)
# ════════════════════════════════════════════

def show_stats():
    """Display vault statistics using tuples and sets."""
    print_header("📊 VAULT STATISTICS")

    if not contacts:
        print("  No contacts to analyze.")
        return

    # Use SET for unique cities count
    unique_cities = get_all_cities()

    # Use TUPLE for a snapshot of all contact names
    all_names = tuple(
        data["name"] for data in contacts.values()
    )

    # City distribution using dictionary
    city_count = {}
    for data in contacts.values():
        city = data["city"]
        city_count[city] = city_count.get(city, 0) + 1

    print(f"  Total Contacts  : {len(contacts)}")
    print(f"  Unique Cities   : {len(unique_cities)}")
    print(f"  Cities          : {', '.join(sorted(unique_cities))}")
    print()
    print("  Contacts per City:")
    print_line()
    for city, count in sorted(city_count.items()):
        bar = "█" * count
        print(f"  {city:<15}: {bar} ({count})")
    print_line()
    print(f"  All Names (tuple snapshot):")
    print(f"  {all_names}")


# ════════════════════════════════════════════
#   MAIN MENU
# ════════════════════════════════════════════

def main():
    """Main menu loop."""
    while True:
        print()
        print("╔══════════════════════════════════════╗")
        print("        📒 SMART CONTACT VAULT           ")
        print("╠══════════════════════════════════════╣")
        print("  1. View All Contacts                  ")
        print("  2. Add New Contact                    ")
        print("  3. Search Contact                     ")
        print("  4. Update Contact                     ")
        print("  5. Delete Contact                     ")
        print("  6. Browse by City                     ")
        print("  7. Stats & Summary                    ")
        print("  8. Exit                               ")
        print("╚══════════════════════════════════════╝")

        choice = input("\n  Choose option (1-8): ").strip()

        if   choice == "1": view_all_contacts()
        elif choice == "2": add_contact()
        elif choice == "3": search_contact()
        elif choice == "4": update_contact()
        elif choice == "5": delete_contact()
        elif choice == "6": browse_by_city()
        elif choice == "7": show_stats()
        elif choice == "8":
            print("\n  👋 Goodbye! Contacts saved. Exiting...\n")
            break
        else:
            print("\n  ❌ Invalid option. Please choose 1-8.")


# ── Run the program ──────────────────────────────────────────────
if __name__ == "__main__":
    main()
    