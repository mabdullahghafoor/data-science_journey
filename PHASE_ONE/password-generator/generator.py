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
