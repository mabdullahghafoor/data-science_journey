import random
import string


def generate_password(length=12,
                      use_upper=True,
                      use_digits=True,
                      use_symbols=True):
    """
    Generate a secure random password.
    """

    characters = string.ascii_lowercase

    if use_upper:
        characters += string.ascii_uppercase

    if use_digits:
        characters += string.digits

    if use_symbols:
        characters += string.punctuation

    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password


def check_strength(password):
    """
    Returns:
    Weak, Medium, Strong, Very Strong
    """

    score = 0

    if len(password) >= 8:
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(char in string.punctuation for char in password):
        score += 1

    if score == 1:
        return "Weak"

    elif score == 2:
        return "Medium"

    elif score == 3:
        return "Strong"

    else:
        return "Very Strong"


def generate_pin(digits=6):
    """
    Generate numeric PIN.
    """

