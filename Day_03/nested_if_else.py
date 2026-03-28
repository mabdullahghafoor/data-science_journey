# In tis we willsolve some nested if else examples

print()
age = int(input("Enter your Age: "))
salary = int(input("Enter your Salary: "))
credit_score = int(input("Enter your Credit score: "))

if (age >= 21):
    if (salary >= 50000):
        if(credit_score >= 700):
            print(f"\n✅ Loan Approved!. Congratulations🎉.")
        else:
            print(f"\n❌ Your Credit Score is too low.")
    else:
        print(f"\n❌ Your Salary is below requirement for the loan.")
else:
    print(f"\n❌ You must be atleast 21 years old.")