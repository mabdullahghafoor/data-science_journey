# In this we will do a mini challenge for practicing operators

'''
> **"Smart Tax Calculator — Pakistan FBR Style"**

Write a program that calculates income tax based on these slabs:

| Annual Income | Tax Rate |
|--------------|----------|
| Up to PKR 600,000 | 0% |
| PKR 600,001 – 1,200,000 | 5% of amount exceeding 600,000 |
| PKR 1,200,001 – 2,400,000 | PKR 30,000 + 10% exceeding 1,200,000 |
| Above PKR 2,400,000 | PKR 150,000 + 15% exceeding 2,400,000 |

Program should print:
```
╔══════════════════════════════════════╗
         💰 TAX CALCULATOR — FBR
╠══════════════════════════════════════╣
  Annual Income : PKR 1,500,000
  Tax Slab      : Slab 3
  Tax Amount    : PKR   60,000
  After-Tax     : PKR 1,440,000
  Effective Rate: 4.0%
╚══════════════════════════════════════╝
'''

income = int(input("Enter Your Income: "))

if income < 0:
    print("Invalid income!")

else:
    # ✅ Decide slab + tax_amount only
    if income <= 600000:
        slab = "Slab 1"
        tax_amount = 0

    elif income <= 1200000:
        slab = "Slab 2"
        tax_amount = (income - 600000) * 0.05

    elif income <= 2400000:
        slab = "Slab 3"
        tax_amount = 30000 + (income - 1200000) * 0.10

    else:
        slab = "Slab 4"
        tax_amount = 150000 + (income - 2400000) * 0.15

    # ✅ Calculate once (efficient)
    after_tax = income - tax_amount
    effective_rate = (tax_amount / income) * 100 if income != 0 else 0

    # ✅ Output
    print("\n╔══════════════════════════════════════╗")
    print("        💰 TAX CALCULATOR — FBR")
    print("╠══════════════════════════════════════╣")
    print(f"  Annual Income : PKR {income:,.2f}")
    print(f"  Tax Slab      : {slab}")
    print(f"  Tax Amount    : PKR {tax_amount:,.2f}")
    print(f"  After-Tax     : PKR {after_tax:,.2f}")
    print(f"  Effective Rate: {effective_rate:.2f}%")
    print("╚══════════════════════════════════════╝")