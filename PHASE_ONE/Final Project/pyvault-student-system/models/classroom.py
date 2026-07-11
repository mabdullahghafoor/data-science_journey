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

    # ── CRUD Operations ───────────────────────────────────────────
    def add_student(self, student):
        """Add student to classroom hashmap."""
        if student.student_id in self.__students:
            raise ValueError(
                f"ID '{student.student_id}' already exists!"
            )
        self.__students[student.student_id] = student
        self.__save()
        print(f"\n  ✅ Student '{student.name}' added!")

    def get_student(self, student_id):
        """Get student by ID — O(1) hashmap lookup."""
        if student_id not in self.__students:
            raise KeyError(f"Student '{student_id}' not found!")
        return self.__students[student_id]

    def update_student(self, student_id, **kwargs):
        """Update student fields."""
        student = self.get_student(student_id)
        for field, value in kwargs.items():
            if hasattr(student, field):
                setattr(student, field, value)
        self.__save()
        print(f"\n  ✅ Student '{student.name}' updated!")

    def delete_student(self, student_id):
        """Remove student from system."""
        student = self.get_student(student_id)
        name    = student.name
        del self.__students[student_id]
        Student.total_count -= 1
        self.__save()
        print(f"\n  ✅ '{name}' removed from system!")

    def add_marks(self, student_id, subject, marks):
        """Add marks for a student."""
        student = self.get_student(student_id)
        student.add_marks(subject, marks)
        self.__save()

    # ── Search & Filter ───────────────────────────────────────────
    def search_by_name(self, query):
        """Linear search by name — O(n)."""
        query   = query.lower()
        results = [
            s for s in self.__students.values()
            if query in s.name.lower()
        ]
        return results

    def get_by_city(self, city):
        """Filter students by city using lambda."""
        return list(filter(
            lambda s: s.city.lower() == city.lower(),
            self.__students.values()
        ))

    def get_all_cities(self):
        """Return unique cities using SET."""
        return sorted(set(
            s.city for s in self.__students.values()
        ))

    # ── DSA: Sorting ──────────────────────────────────────────────
    def get_ranked(self, reverse=True):
        """
        Sort students by percentage.
        Uses sorted() with lambda key — O(n log n)
        """
        students = [
            s for s in self.__students.values()
            if s.has_marks()
        ]
        return sorted(
            students,
            key=lambda s: s.percentage,
            reverse=reverse
        )

    # ── Analytics ────────────────────────────────────────────────
    def get_topper(self):
        """Return student with highest percentage."""
        ranked = self.get_ranked()
        return ranked[0] if ranked else None

    def get_failures(self):
        """Return list of failed students using filter."""
        return list(filter(
            lambda s: s.has_marks() and "Fail" in s.status,
            self.__students.values()
        ))

    def class_average(self):
        """Calculate class average percentage."""
        students = [
            s for s in self.__students.values()
            if s.has_marks()
        ]
        if not students:
            return 0.0
        return round(
            sum(s.percentage for s in students) / len(students),
            2
        )

    def grade_distribution(self):
        """
        Count students per grade using HASHMAP.
        Demonstrates frequency counting DSA pattern.
        """
        distribution = {}
        for student in self.__students.values():
            if student.has_marks():
                grade = student.grade
                distribution[grade] = (
                    distribution.get(grade, 0) + 1
                )
        return distribution

    def subject_averages(self):
        """Calculate average per subject."""
        subject_totals = {}
        subject_counts = {}

        for student in self.__students.values():
            for subject, marks in student.get_marks().items():
                subject_totals[subject] = (
                    subject_totals.get(subject, 0) + marks
                )
                subject_counts[subject] = (
                    subject_counts.get(subject, 0) + 1
                )

        return {
            subject: round(
                subject_totals[subject] / subject_counts[subject],
                2
            )
            for subject in subject_totals
        }

    def total_students(self):
        return len(self.__students)

    def get_all_students(self):
        return list(self.__students.values())

    # ── File Persistence ──────────────────────────────────────────
    def __save(self):
        """Save all students to JSON file."""
        try:
            os.makedirs("data", exist_ok=True)
            data = {
                sid: s.to_dict()
                for sid, s in self.__students.items()
            }
            with open(self.DATA_FILE, "w",
                      encoding="utf-8") as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            print(f"  ⚠️  Save failed: {e}")

    def __load(self):
        """Load students from JSON file on startup."""
        try:
            if os.path.exists(self.DATA_FILE):
                with open(self.DATA_FILE, "r",
                          encoding="utf-8") as f:
                    data = json.load(f)
                for sid, sdata in data.items():
                    student = Student.from_dict(sdata)
                    self.__students[sid] = student
        except (json.JSONDecodeError, KeyError) as e:
            print(f"  ⚠️  Load error: {e}. Starting fresh.")