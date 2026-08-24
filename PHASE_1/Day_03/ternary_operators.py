# In tis we will solve some ternay operators (one liner if-ele) examples

# Long-Version

marks = 75

if (marks >= 50):
    print("PASS")
else:
    print("FAIL")

# Short-Version (Ternay OPerator Option)

result = "PASS" if marks >= 50 else "FAIL"
print(result)

# More Examples

age = 20
status = "Adult" if age >=18 else "Minor"
print(status)

number = 7
parity = "Even" if number % 2 == 0 else ("Odd")
print(parity) 