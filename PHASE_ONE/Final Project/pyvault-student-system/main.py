# ═══════════════════════════════════════════════════
# FILE    : main.py
# PROJECT : PyVault — Student Management System
# AUTHOR  : Your Name
# PHASE   : 1 — Python Foundation (Final Project)
# USES    : ALL 15 TOPICS
# ═══════════════════════════════════════════════════

import os
from datetime import datetime
from models.students    import Student
from models.classroom  import Classroom
from utils.validators  import (get_input, get_int,
                                validate_email,
                                validate_student_id)
from utils.analytics   import (get_top_n_stack,
                                announcement_queue,
                                grade_frequency_hashmap)

# ── Initialize classroom ──────────────────────────────────────────
classroom = Classroom()


