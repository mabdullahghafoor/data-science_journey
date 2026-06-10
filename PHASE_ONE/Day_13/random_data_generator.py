import random

names = [
    "Ali", "Ahmed", "Sara", "Ayesha",
    "Fatima", "Usman", "Bilal", "Hina"
]


def random_name():
    return random.choice(names)


def random_marks(n):
    marks = []

    for i in range(n):
        marks.append(random.randint(50, 100))

    return marks
