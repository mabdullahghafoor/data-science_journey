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


def remove_duplicates(text):
    words = text.split()
    unique_words = []

    for word in words:
        if word not in unique_words:
            unique_words.append(word)

    return " ".join(unique_words)