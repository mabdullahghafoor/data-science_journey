# In this program we will solve hard level practice problems of Sets


#Q7. You are given 4 weeks of website visitor data (user IDs):
#Find:
#Visitors who came ALL 4 weeks (loyal users)
#Visitors who came only ONCE across all weeks
#Total unique visitors across all 4 weeks
#New visitors each week (not seen in previous weeks)

week1 = {101,102,103,104,105,106}
week2 = {103,104,105,107,108,109}
week3 = {105,106,108,110,111,112}
week4 = {101,105,109,110,113,114}
#1.
loyal_visitors = week1 & week2 & week3 & week4

only_once = []
multiple_time = []

for id in week1:

    if id in week2:
        multiple_time.append(id)
    elif id in week3:
        multiple_time.append(id)
    elif id in week4:
        multiple_time.append(id)
    else:
        only_once.append(id)

#3.
unique_visitors = week1 | week2 | week3 | week4

total_unique_visitors = len(unique_visitors)
#4.
new_week2 = week2 - week1
new_week3 = week3 - week2
new_week4 = week4 - week3

print(f"Loyal Visitors : {loyal_visitors}")
print(f"Visitor Comes Only Once: {only_once}")
print(f"Total Unique Visitors Across All Weeks : {total_unique_visitors}")
print(f"New Visitor in Week 2: {new_week2}")
print(f"New Visitor in Week 3: {new_week3}")
print(f"New Visitor in Week 4: {new_week4}")


