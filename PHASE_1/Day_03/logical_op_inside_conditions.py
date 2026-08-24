# In tis we will solve some logical operators inside conditional statement examples

print()
age = int(input("Enter your Age: "))
salary = int(input("Enter your Monthly Salary: "))
credit_score = int(input("Enter your Credit score: "))

if (age >= 21) and (salary >= 50000) and (credit_score >= 700):
    print(f"✅ Loan Approved!. Congratulations! 🎉") 

elif (age >= 21) and (salary >= 50000):
    print(f"⚠️  Approved with Higher interest rates.")

else:
    print(f" ❌ Loan Rejected!")