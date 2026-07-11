# ═══════════════════════════════════════════════════
# FILE    : models/classroom.py
# PURPOSE : Classroom — manages collection of students
# USES    : OOP, DSA, Lambda, File Handling
# ═══════════════════════════════════════════════════

import json
import os
from models.students import Student


class Classroom:
    """
    Manages a collection of students.
    Demonstrates: OOP, DSA algorithms, File I/O
    """

    DATA_FILE = "data/students.json"

    def __init__(self):
        self.__students = {}    # hashmap: id → Student object
        self.__load()           # load from file on startup

