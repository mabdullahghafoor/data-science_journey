# In this program we will perform a mini challenge for tuple

# Create a system using tuples that stores flight records:
# Print a formatted flight board and answer:
# - Most expensive flight
# - Cheapest flight
# - All flights FROM Karachi
# - Average ticket price


flights = (
    ("PK-301", "Karachi",   "Lahore",    1550, "06:00 AM"),
    ("PK-402", "Lahore",    "Islamabad",  980, "09:30 AM"),
    ("PK-505", "Karachi",   "Islamabad", 1800, "11:00 AM"),
    ("PK-610", "Islamabad", "Lahore",     950, "02:00 PM"),
    ("PK-712", "Lahore",    "Karachi",   1600, "05:30 PM"),
)




print(f"╔═══════════════════════════════════════════════════════╗")
print(f"            ✈️  PAKISTAN AIRLINES — FLIGHT BOARD")
print(f"╠═══════════════════════════════════════════════════════╣")
print(f"  Flight  │ From        │ To          │ Price  │ Time")

print(f"  ───────────────────────────────────────────────────────")

karachi_flights = []
price_list = []

for flight,departure,arrival,price,time in flights:

    print(f"  {flight:>5}  | {departure:>11} | {arrival:>11} | {price:>6} | {time:>5}")

    price_list.append(price)

    if departure == "Karachi":
        karachi_flights.append(flight)
        
        

    

expensive = max(price_list)
cheapest = min(price_list)
avg = sum(price_list)/len(price_list)

for flight,departure,arrival,price,time in flights:

    if price == expensive:
        expensive_flight = flight
    elif price == cheapest:
        cheapest_flight = flight
print()
print(f"💰 Most Expensive : {expensive_flight} (Rs{expensive})")
print(f"💸 Cheapest       : {cheapest_flight} (Rs{cheapest})")
print(f"📍 From Karachi   : {karachi_flights[0]}, {karachi_flights[1]}")
print(f"📊 Avg Price      : Rs{avg}")
print(f"╚═══════════════════════════════════════════════════════╝")

