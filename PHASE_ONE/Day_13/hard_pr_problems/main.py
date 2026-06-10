from utils import calculate_percentage, get_grade
from validators import validate_name, validate_marks
from reporter import print_card, print_summary

name = "Ali"
marks = [85, 90, 78, 88, 92]

if validate_name(name) and validate_marks(marks):

    percentage = calculate_percentage(marks)
    grade = get_grade(percentage)

