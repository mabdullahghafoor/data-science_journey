# In tis we willsolve some if elif and else examples

marks = int(input("Enter your marks(0-100): "))

if (marks >= 90):
    grade = "A+"
    remarks = "Outstanding!🌟"

elif (marks >= 80):
    grade = "A"
    remarks = "Excellent!🎉"

elif (marks >= 70):
    grade = "B"
    remarks = "Good work!👍🏻"

elif (marks >= 60):
    grade = "C"
    remarks = "Satisfactory!"

elif (marks >= 50):
    grade = "D"
    remarks = "PASS, but hardwork needed!"

else:
    grade = "F"
    remarks = "FAIL!❌, but keep trying."
    


print(f"\nGrade : {grade}")
print(f"Remarks : {remarks}")

