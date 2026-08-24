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

submitted = [101,102,103,101,104,102,105,103,106]
registered = {101,102,103,104,105,106,107,108}

submitted_set = set(submitted)
# 1.
seen = set()
duplicates = set()
submitted_set = set(submitted)

for rollno in submitted:

    if rollno in seen:
        duplicates.add(rollno)
    else:
        seen.add(rollno)


# 2.

not_register = submitted_set - registered

# 3.

not_submitted = registered - submitted_set


print(F"Labelled Result")
print(f"Duplicates Roll No                          : {duplicates}")
print(f"Students who submitted but NOT registered   : {not_register}") 
print(f"Students who registered but NOT submitted   : {not_submitted}") 



# Q6. Build a skill matcher — given a job's required skills and a candidate's skills, tell:

# Matching skills (candidate has these ✅)
# Missing skills (candidate needs these ❌)
# Extra skills (candidate has bonus skills ⭐)

job_skills = {"python", "sql", "git", "linux"}
candidate_skills = {"python", "git", "excel", "communication"}

matching_skills = job_skills & candidate_skills
missing_skills = job_skills - candidate_skills
extra_skills = candidate_skills - job_skills

print(f"Matching Skills : {matching_skills}")
print(f"Missing Skills  : {missing_skills}")
print(f"Extra Skills    : {extra_skills}")

