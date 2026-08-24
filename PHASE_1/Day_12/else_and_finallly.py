# In this we will se  how to use else and finally

# ── Full exception handling structure ────────────────────────────
#
#   try:      → risky code
#   except:   → runs IF error occurs
#   else:     → runs ONLY IF no error occurred
#   finally:  → ALWAYS runs (error or not) — for cleanup
#

try:
    marks = int(input("Enter marks (0-100): "))

    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100")

    percentage = (marks / 100) * 100

except ValueError as e:
    print(f"❌ Invalid input: {e}")

else:
    # Only runs if try block had NO errors
    print(f"✅ Marks accepted: {marks}")
    print(f"   Percentage   : {percentage:.1f}%")

finally:
    # ALWAYS runs — perfect for cleanup
    print("─" * 35)
    print("Processing complete.")

