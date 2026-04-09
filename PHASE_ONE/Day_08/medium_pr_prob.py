# In this program we will solve some medium level practice problems of Sets

# Q4. Build a student gradebook using a dictionary. 
# Store 5 students with their marks list. 
# Loop through and print each student's 
# average, grade, and pass/fail status.


gradebook = {
    "Ali" : [66,78,82,77,80],
    "Sara" : [88,73,75,80,79],
    "Aima" : [83,85,75,67,69],
    "Faraz" : [55,63,69,52,50],
    "Taha" : [45,55,63,14,51,40]
}

for name, marks in gradebook.items():
    average = sum(marks)/len(marks)

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"    
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    if average >= 50:
        status = "Pass"
    else:
        status = "Fail"

    print(f"Name : {name}  Average : {average:.2f}  Grade : {grade}  {status}")


# Q5. Write a word frequency counter for this sentence:
# Print each word and how many times it appears, 
# sorted from most to least frequent.

text = "to be or not to be that is the question to be"

words = text.split()

frequency = {}

for word in words:
    
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print(f"{frequency}")

# Q6. Given this dictionary of monthly sales:
# Find and print: best month, worst month, total annual sales, 
# average monthly sales, and all months above average.

sales = {"Jan":120000, "Feb":95000,  "Mar":140000,
         "Apr":88000,  "May":175000, "Jun":160000,
         "Jul":132000, "Aug":145000, "Sep":98000,
         "Oct":185000, "Nov":170000, "Dec":210000}

best_sale = sales["Jan"]
worst_sale = sales["Jan"]
total = 0
abv_avg_mon = []

for month,sale in sales.items():

    if sale > best_sale:
        best_month = month
        best_sale = sales[month]
    elif sale < worst_sale:
        worst_month = month
        worst_sale = sales[month]

    total += sale

    average = total / 12
    if sale > average: 
        abv_avg_mon.append(month)

  

print(f"Best Sale Month     : {best_month}  Sale : {best_sale}")
print(f"Worst Sale Month    : {worst_month}  Sale : {worst_sale}")
print(f"Total Annual Sale   : {total}")
print(f"Average Monthly Sale: {average:.2f}")
print(f"Above Average Months: {abv_avg_mon}")    




    