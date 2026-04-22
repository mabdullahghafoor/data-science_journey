# In This Program we will see how to solve hard level practice problems of lamda functions

#Q7. You have this sales data:
#Using only lambda, map, filter, sorted:

#Calculate total revenue per product (price × qty)
#Filter products with revenue > PKR 100,000#
#Sort by revenue highest first
#Print a formatted sales report


sales = [
    {"product": "Laptop",   "price": 85000, "qty": 5,  "city": "Karachi"},
    {"product": "Mouse",    "price":  1500, "qty": 50, "city": "Lahore"},
    {"product": "Keyboard", "price":  3500, "qty": 30, "city": "Karachi"},
    {"product": "Monitor",  "price": 45000, "qty": 8,  "city": "Lahore"},
    {"product": "Webcam",   "price":  8000, "qty": 15, "city": "Islamabad"},
]

#Calculate total revenue per product (price × qty)
revenu = list(map(lambda x : (x["price"] * x["qty"]) , sales))
total_revenu = []
for s in revenu:
    print(f"{s}")
    total_revenu.append(s)


print()
#Filter products with revenue > PKR 100,000#

selected = list(filter(lambda x: (x > 100000), total_revenu))

for f in selected:
    print(f)

print()
#Sort by revenue highest first

highest = sorted(total_revenu, key=lambda x: x, reverse=True)

print(highest)