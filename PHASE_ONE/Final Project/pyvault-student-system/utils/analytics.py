# ═══════════════════════════════════════════════════
# FILE    : utils/analytics.py
# PURPOSE : DSA algorithms for data analysis
# USES    : DSA — Search, Sort, Stack, Hashmap
# ═══════════════════════════════════════════════════

from collections import deque


def binary_search_by_id(students_list, target_id):
    """
    Binary search on sorted student list by ID.
    O(log n) time complexity.
    """
    sorted_list = sorted(students_list,
                         key=lambda s: s.student_id)
    left, right = 0, len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid].student_id == target_id:
            return sorted_list[mid]
        elif sorted_list[mid].student_id < target_id:
            left = mid + 1
        else:
            right = mid - 1
    return None


def get_top_n_stack(students, n=5):
    """
    Use STACK to get top N students.
    Push all → pop top N.
    """
    stack   = []
    ranked  = sorted(students,
                     key=lambda s: s.percentage)

    for student in ranked:
        stack.append(student)   # push all

    top_n = []
    count = min(n, len(stack))
    for _ in range(count):
        top_n.append(stack.pop())   # pop top N
    return top_n


def announcement_queue(students):
    """
    Use QUEUE to simulate result announcement.
    Highest scorer announced last (most dramatic!).
    """
    ranked = sorted(students,
                    key=lambda s: s.percentage)
    queue  = deque(ranked)      # lowest first
    order  = []
    while queue:
        order.append(queue.popleft())
    return order


def grade_frequency_hashmap(students):
    """
    Count grade frequencies using HASHMAP.
    Classic frequency counter DSA pattern.
    """
    freq = {}
    for student in students:
        if student.has_marks():
            grade      = student.grade
            freq[grade] = freq.get(grade, 0) + 1
    return dict(sorted(freq.items()))