def is_palindrome(text):
    text = text.lower()
    return text == text[::-1]


def word_count(text):
    words = text.split()
    counts = {}

    for word in words:
        counts[word] = counts.get(word, 0) + 1

    return counts


def capitalize_words(text):
    return text.title()


