# In this program we will solve some medium level practice problems of Sets


# Q4. Given two sets:
# Print clearly labeled results for: 
# union, intersection, difference (both ways), symmetric difference.


morning_students = {"Ali", "Sara", "Fatima", "Omar", "Zara"}
evening_students = {"Sara", "Omar", "Bilal", "Hina", "Fatima"}

# Union
union = morning_students | evening_students

# Intersection 
intersection = morning_students & evening_students

# Difference
diff_mor_to_eve = morning_students - evening_students
diff_eve_to_mor = evening_students - morning_students 

# Symmetric Difference
symmetric = morning_students ^ evening_students

print(f"Labelled Result")
print(f"Union                : {union}")
print(f"Intersection         : {intersection}")
print(f"Difference Mor To Eve: {diff_mor_to_eve}")
print(f"Difference Eve To Mor: {diff_eve_to_mor}")
print(f"Symmetric Difference : {symmetric}")


# Q5. You have a list of exam roll numbers 
# with some errors (duplicates). Use sets to:
# Find who submitted more than once (duplicates)
# Find who submitted but is NOT registered
# Find registered students who did NOT submit

