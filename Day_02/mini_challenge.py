# In this we will do a mini challenge for practicing operators
'''
> **"Smart Electricity Bill Calculator"**

A utility company charges as follows:
- First 100 units → PKR 5 per unit
- Next 100 units (101–200) → PKR 8 per unit
- Above 200 units → PKR 12 per unit
- Fixed service charge → PKR 150

Write a program that:
- Takes units consumed as input
- Calculates total bill using operators
- Prints a detailed formatted bill

**Example Output:**
```
╔══════════════════════════════════╗
        ⚡ ELECTRICITY BILL
╠══════════════════════════════════╣
  Units Consumed  : 250
  First 100 units : PKR  500.00
  Next  100 units : PKR  800.00
  Above 200 units : PKR  600.00
  Service Charge  : PKR  150.00
─────────────────────────────────
  TOTAL BILL      : PKR 2050.00
╚══════════════════════════════════╝
'''


units = int(input("Enter your units: "))




cond1 = (((units < 100) and (units*5)) or (100*5))

cond2 = (
    (units <= 100 and 0) or
    (100 < units <= 200 and (units - 100) * 8) or
    (units > 200 and 100 * 8)
)

cond3 = (
    (units <= 200 and 0) or
    (units >200 and (units - 200) * 12)
)

service_charges = 150

total_bill = cond1 + cond2 +cond3 + service_charges

print()
print()
print()
print("╔════════════════════════════════════╗")
print("          ⚡ ELECTRICITY BILL   ")
print("╠════════════════════════════════════╣")
print(f"    Units Consumed    : {units}")
print(f"    First 100 units   : {cond1:.2f}")
print(f"    Next  100 units   : {cond2:.2f}")
print(f"    Above 200 units   : {cond3:.2f}")
print(f"    Service Charges   : {service_charges:.2f}")
print(f"─────────────────────────────────────")
print(f"    TOTAL BILL        : {total_bill:.2f}")
print("╚════════════════════════════════════╝")
print()
print()
print()
