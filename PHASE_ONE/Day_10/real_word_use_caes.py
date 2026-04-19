# In this we will se how to use lambda functio in Real World Basic things

# ── Use Case 1: Sort products by price ───────────────────────────
products = [
    ("Laptop",  85000),
    ("Mouse",    1500),
    ("Keyboard", 3500),
    ("Monitor", 45000),
    ("Webcam",   8000),
]

cheapest   = sorted(products, key=lambda p: p[1])
expensive  = sorted(products, key=lambda p: p[1], reverse=True)

print("💸 Cheapest first:")
for name, price in cheapest:
    print(f"  {name:<12}: PKR {price:,}")