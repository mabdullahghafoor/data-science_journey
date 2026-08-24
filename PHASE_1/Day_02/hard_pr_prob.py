# In This program we will solve some hard practice problems for operators

'''
Q7.** Build a **BMI Calculator** that:
- Takes weight (kg) and height (m) as input
- Calculates BMI: `weight / height²`
- Prints the BMI value formatted to 2 decimals
- Prints the category using comparisons:
  - BMI < 18.5 → Underweight
  - 18.5–24.9 → Normal
  - 25–29.9 → Overweight
  - 30+ → Obese
'''

weight = float(input("Enter your weight: "))
height = float(input("Enter your height in feets: "))

height_m = height * 0.3048

bmi = weight / (height_m**2)

print(f"Your BMI = {bmi:.2f}")
print(
    ((bmi < 18.5) and "Underweight") or
    ((bmi >= 18.5 and bmi <= 24.9) and "Normal") or
    ((bmi >= 25 and bmi <= 29.9) and "Overweight") or
    ((bmi >= 30) and "Obese")
    )
