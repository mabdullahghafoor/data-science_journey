# In this program we will see some logical operators examples

age = 20
has_id = True
is_member = False

# AND - Both conditions must be true
print(age >= 18 and has_id)
print(age >= 18 and is_member)

# OR - At least one condition be true
print(age >= 18 or is_member)
print (age < 18 or is_member)

# NOT - Reverse the result
print(not is_member)
print(not has_id)

# Real World Example
salary = 80000
credit_score = 720
has_job = True

eligibility = salary >= 50000 and credit_score >= 700 and has_job
print(f"Loan Eligibility: {eligibility}")

