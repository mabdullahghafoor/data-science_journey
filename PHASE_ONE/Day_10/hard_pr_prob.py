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

# Step 1: Add revenue to each product
with_revenue = list(map(
    lambda x: {**x, "revenue": x["price"] * x["qty"]}, #--> **x takes everything from x
    sales
))
 
# Step 2: Filter revenue > 100000
filtered = list(filter(
    lambda x: x["revenue"] > 100000,
    with_revenue
))

# Step 3: Sort by revenue (highest first)
sorted_data = sorted(
    filtered,
    key=lambda x: x["revenue"],
    reverse=True
)

# Step 4: Print formatted report
print("=== SALES REPORT ===")
for item in sorted_data:
    print(f"{item['product']:10} | City: {item['city']:10} | Revenue: PKR {item['revenue']:,}")


    