# In this we will see how to create our own package

# FILE: main.py — using the package
from students_system import utils
from students_system.grades import assign_grade
from students_system.reports import generate_report_header

generate_report_header("Student Performance Report")
