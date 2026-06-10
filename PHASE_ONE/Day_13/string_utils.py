def is_palindrome(text):
    text = text.lower()
    return text == text[::-1]


def word_count(text):
    words = text.split()
    counts = {}

