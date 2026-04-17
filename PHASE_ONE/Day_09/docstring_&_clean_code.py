# In This Program we will see how can we write a docstring and a clean code

# ── Docstrings: explain your function professionally ─────────────
# This is what appears when someone calls help(your_function)

def calculate_bmi(weight_kg, height_m):

    """
    Calculate Body Mass Index (BMI).

    Parameters:
        weight_kg (float): Weight in kilograms
        height_m  (float): Height in meters

    Returns:
        tuple: (bmi_value, category)

    Example:
        >>> bmi, category = calculate_bmi(70, 1.75)
        >>> print(bmi)
        22.86
    """
    bmi = weight_kg / (height_m ** 2)

    if   bmi < 18.5: category = "Underweight"
    elif bmi < 25.0: category = "Normal ✅"
    elif bmi < 30.0: category = "Overweight"
    else:            category = "Obese"

    return round(bmi, 2), category


# ── Using the function ───────────────────────────────────────────
bmi, category = calculate_bmi(70, 1.75)
print(f"BMI: {bmi} → {category}")


# ── Access the docstring ─────────────────────────────────────────
print(calculate_bmi.__doc__)