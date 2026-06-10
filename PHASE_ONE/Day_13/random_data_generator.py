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


def random_student():
    student = {
        "name": random_name(),
        "age": random.randint(15, 20),
        "marks": random_marks(5)
    }

    return student


def random_class(size):
    students = []

    for i in range(size):
        students.append(random_student())

    return students