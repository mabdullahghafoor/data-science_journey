# In this program we will solve some medium level practice problems of tuples


# Q7. You are given monthly sales data as a tuple 
# (cannot change — it's historical data):
                                                 
# Write a program that prints:

# Best month (name + sales)
# Worst month (name + sales)
# Total annual sales
# Average monthly sales
# Months that were above average

monthly_sales = (120000, 95000, 140000, 88000, 175000,160000,
                132000, 145000, 98000, 185000,170000, 210000)

months = ("Jan","Feb","Mar","Apr","May","Jun",
          "Jul","Aug","Sep","Oct","Nov","Dec")


max_sale = max(monthly_sales)

min_sale = min(monthly_sales)

total_annual_sale = sum(monthly_sales)

avg_monthly_sale = total_annual_sale/len(monthly_sales)

max_index = monthly_sales.index(max_sale)

min_index = monthly_sales.index(min_sale)

above_avg_month = []

for sale in monthly_sales:
    if sale > avg_monthly_sale:
        above = monthly_sales.index(sale)
        above_month = months[above]
        above_avg_month.append(above_month)



print(f"SUMMARY")
print(f"Best Month = {months[max_index]}     Best Sale = {max_sale}")
print(f"Worst Month = {months[min_index]}    Best Sale = {min_sale}")
print(f"Total annual sales = {total_annual_sale}")
print(f"Avergae Monthly Sale = {avg_monthly_sale:.2f}")
print(f"Above Average Sales Moths Are : {above_avg_month}")


