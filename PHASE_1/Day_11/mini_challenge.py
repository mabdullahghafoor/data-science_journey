# In this we sill do a mini challenge




import json
import os
from datetime import datetime

FILE_NAME = "expenses.json"

# ---------- Core Functions ----------

def load_expenses():
    """Load expenses from JSON file."""
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return json.load(f)


def save_expenses(expenses):
    """Save expenses to JSON file."""
    with open(FILE_NAME, "w") as f:
        json.dump(expenses, f, indent=4)


def add_expense(category, description, amount):
    """Add new expense with auto timestamp."""
    expenses = load_expenses()
    
    expense = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "category": category,
        "description": description,
        "amount": amount
    }
    
    expenses.append(expense)
    save_expenses(expenses)
    print("✅ Expense added successfully!")


def view_expenses():
    """Display all expenses in formatted table."""
    expenses = load_expenses()
    
    if not expenses:
        print("No expenses found.")
        return
    
    print("\n╔══════════════════════════════════════════════╗")
    print("         💰 PERSONAL EXPENSE TRACKER")
    print("╠══════════════════════════════════════════════╣")
    print(f"{'Date':<12}{'Category':<12}{'Description':<15}{'Amount'}")
    print("──────────────────────────────────────────────")
    
    for exp in expenses:
        print(f"{exp['date']:<12}{exp['category']:<12}{exp['description']:<15}Rs {exp['amount']}")
    
    print("╚══════════════════════════════════════════════╝")


def get_summary():
    """Show total spent and category breakdown."""
    expenses = load_expenses()
    
    if not expenses:
        print("No data available.")
        return
    
    total = sum(exp["amount"] for exp in expenses)
    
    category_totals = {}
    for exp in expenses:
        cat = exp["category"]
        category_totals[cat] = category_totals.get(cat, 0) + exp["amount"]
    
    print("\n╠══════════════════════════════════════════════╣")
    print("  SUMMARY")
    print(f"  Total Spent  : Rs {total}")
    
    for cat, amt in category_totals.items():
        percent = (amt / total) * 100
        print(f"  {cat:<12}: Rs {amt}   ({percent:.1f}%)")
    
    print("╚══════════════════════════════════════════════╝")


def export_to_txt():
    """Export readable report to expenses_report.txt."""
    expenses = load_expenses()
    
    if not expenses:
        print("No data to export.")
        return
    
    total = sum(exp["amount"] for exp in expenses)
    
    category_totals = {}
    for exp in expenses:
        cat = exp["category"]
        category_totals[cat] = category_totals.get(cat, 0) + exp["amount"]
    
    with open("expenses_report.txt", "w") as f:
        f.write("PERSONAL EXPENSE REPORT\n\n")
        
        for exp in expenses:
            f.write(f"{exp['date']} | {exp['category']} | {exp['description']} | Rs {exp['amount']}\n")
        
        f.write("\n--- SUMMARY ---\n")
        f.write(f"Total Spent: Rs {total}\n")
        
        for cat, amt in category_totals.items():
            percent = (amt / total) * 100
            f.write(f"{cat}: Rs {amt} ({percent:.1f}%)\n")
    
    print("📄 Report exported successfully!")


# ---------- Menu System ----------

def menu():
    while True:
        print("\n=== EXPENSE TRACKER ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Summary")
        print("4. Export Report")
        print("5. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            cat = input("Category: ")
            desc = input("Description: ")
            amt = float(input("Amount: "))
            add_expense(cat, desc, amt)
        
        elif choice == "2":
            view_expenses()
        
        elif choice == "3":
            get_summary()
        
        elif choice == "4":
            export_to_txt()
        
        elif choice == "5":
            print("Goodbye 👋")
            break
        
        else:
            print("Invalid choice!")


# ---------- Run ----------
menu()

