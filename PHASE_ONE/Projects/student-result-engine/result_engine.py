# ═══════════════════════════════════════════════════════════════
# PROJECT  : Student Result Engine
# PURPOSE  : Process student marks and generate report card
# AUTHOR   : Your Name
# PHASE    : 1 — Python Foundation (Topics 1, 2, 3)
# ═══════════════════════════════════════════════════════════════


# ── CONSTANTS (never change these values) ──────────────────────
PASS_MARK       = 40        # minimum marks to pass a subject
PASS_PERCENTAGE = 50        # minimum % to pass overall
MAX_MARKS       = 100       # maximum marks per subject
SUBJECTS        = 5         # total number of subjects


# ── HELPER: Display separator line ─────────────────────────────
def print_line():
    print("─" * 42) 


# ══════════════════════════════════════════
#   STEP 1 — COLLECT STUDENT INFORMATION
# ══════════════════════════════════════════

print("╔══════════════════════════════════════════╗")
print("       🎓 STUDENT RESULT ENGINE             ")
print("╚══════════════════════════════════════════╝")
print()

student_name = input("Enter student name     : ")
roll_number  = input("Enter roll number      : ")
class_name   = input("Enter class            : ")

print()
print("📝 Enter marks for each subject (out of 100):")
print_line()


# ══════════════════════════════════════════
#   STEP 2 — COLLECT & VALIDATE MARKS
# ══════════════════════════════════════════

# Get marks for each subject with input validation
raw_math    = int(input("   Mathematics        : "))
raw_english = int(input("   English            : "))
raw_science = int(input("   Science            : "))
raw_urdu    = int(input("   Urdu               : "))
raw_cs      = int(input("   Computer Science   : "))


# ── Validate: marks must be between 0 and 100 ──────────────────
valid_input = (
    0 <= raw_math    <= MAX_MARKS and
    0 <= raw_english <= MAX_MARKS and
    0 <= raw_science <= MAX_MARKS and
    0 <= raw_urdu    <= MAX_MARKS and
    0 <= raw_cs      <= MAX_MARKS
)

if not valid_input:
    print("\n❌ ERROR: Marks must be between 0 and 100.")
    print("Please restart and enter valid marks.")

else:
    # ══════════════════════════════════════════
    #   STEP 3 — CALCULATIONS
    # ══════════════════════════════════════════

    # Total and percentage
    total      = raw_math + raw_english + raw_science + raw_urdu + raw_cs
    percentage = (total / (SUBJECTS * MAX_MARKS)) * 100
    average    = total / SUBJECTS

    # ── Grade based on percentage ───────────────────────────────
    if percentage >= 90:
        grade  = "A+"
        remark = "Outstanding! 🌟"
    elif percentage >= 80:
        grade  = "A"
        remark = "Excellent! 🎉"
    elif percentage >= 70:
        grade  = "B"
        remark = "Good Work! 👍"
    elif percentage >= 60:
        grade  = "C"
        remark = "Satisfactory"
    elif percentage >= 50:
        grade  = "D"
        remark = "Passed — work harder"
    else:
        grade  = "F"
        remark = "Failed ❌"

    # ── Check pass/fail per subject ─────────────────────────────
    math_status    = "✅ Pass" if raw_math    >= PASS_MARK else "❌ Fail"
    english_status = "✅ Pass" if raw_english >= PASS_MARK else "❌ Fail"
    science_status = "✅ Pass" if raw_science >= PASS_MARK else "❌ Fail"
    urdu_status    = "✅ Pass" if raw_urdu    >= PASS_MARK else "❌ Fail"
    cs_status      = "✅ Pass" if raw_cs      >= PASS_MARK else "❌ Fail"

    # ── Overall result ──────────────────────────────────────────
    # Student passes ONLY IF all subjects passed AND percentage >= 50
    all_subjects_passed = (
        raw_math    >= PASS_MARK and
        raw_english >= PASS_MARK and
        raw_science >= PASS_MARK and
        raw_urdu    >= PASS_MARK and
        raw_cs      >= PASS_MARK
    )

    overall_result = (
        "🎉 PROMOTED"
        if all_subjects_passed and percentage >= PASS_PERCENTAGE
        else "❌ NOT PROMOTED"
    )


    # ══════════════════════════════════════════
    #   STEP 4 — PRINT REPORT CARD
    # ══════════════════════════════════════════

    print()
    print("╔══════════════════════════════════════════╗")
    print("         📋 OFFICIAL REPORT CARD            ")
    print("╠══════════════════════════════════════════╣")
    print(f"  Student Name : {student_name}")
    print(f"  Roll Number  : {roll_number}")
    print(f"  Class        : {class_name}")
    print("╠══════════════════════════════════════════╣")
    print("  SUBJECT              MARKS    STATUS      ")
    print_line()
    print(f"  Mathematics        :  {raw_math:>3}/100   {math_status}")
    print(f"  English            :  {raw_english:>3}/100   {english_status}")
    print(f"  Science            :  {raw_science:>3}/100   {science_status}")
    print(f"  Urdu               :  {raw_urdu:>3}/100   {urdu_status}")
    print(f"  Computer Science   :  {raw_cs:>3}/100   {cs_status}")
    print("╠══════════════════════════════════════════╣")
    print(f"  Total Marks  : {total} / {SUBJECTS * MAX_MARKS}")
    print(f"  Percentage   : {percentage:.1f}%")
    print(f"  Average      : {average:.1f}")
    print(f"  Grade        : {grade}")
    print(f"  Remark       : {remark}")
    print("╠══════════════════════════════════════════╣")
    print(f"  RESULT       : {overall_result}")
    print("╚══════════════════════════════════════════╝")





