# In This program we will solve some hard practice problems for operators

# **Q7.** Build a **complete student result system**:
# - Input: marks for 5 subjects
# - Calculate total and percentage
# - Assign grade (A+/A/B/C/D/F)
# - Check if passed (all subjects >= 40 AND percentage >= 50)
# - Print a detailed result card
# - Handle invalid input (marks < 0 or > 100)


print("Enter Your subject marks (0 - 100)\n")

sub_1 = int(input("Enter Mark For Subject 1: "))
sub_2 = int(input("Enter Mark For Subject 2: "))
sub_3 = int(input("Enter Mark For Subject 3: "))
sub_4 = int(input("Enter Mark For Subject 4: "))
sub_5 = int(input("Enter Mark For Subject 5: "))

# ✅ Check invalid input (ANY invalid → error)
if (
    (sub_1 < 0 or sub_1 > 100) or
    (sub_2 < 0 or sub_2 > 100) or
    (sub_3 < 0 or sub_3 > 100) or
    (sub_4 < 0 or sub_4 > 100) or
    (sub_5 < 0 or sub_5 > 100)
):
    print("Invalid Marks Entry!")

else:
    obtained_marks = sub_1 + sub_2 + sub_3 + sub_4 + sub_5
    percentage = (obtained_marks / 500) * 100

    # ✅ Grade
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    # ✅ Pass / Fail
    passed = (
        sub_1 >= 40 and sub_2 >= 40 and sub_3 >= 40 and
        sub_4 >= 40 and sub_5 >= 40 and percentage >= 50
    )

    # ✅ Output
    print("\n--------------- REPORT CARD ---------------\n")
    print(f"Subject 1      = {sub_1}")
    print(f"Subject 2      = {sub_2}")
    print(f"Subject 3      = {sub_3}")
    print(f"Subject 4      = {sub_4}")
    print(f"Subject 5      = {sub_5}")
    print()
    print(f"Obtained Marks = {obtained_marks}")
    print("Total Marks    = 500\n")
    print(f"Percentage     = {percentage:.2f}%")
    print(f"Grade          = {grade}")
    print(f"Result         = {'PASS' if passed else 'FAIL'}")