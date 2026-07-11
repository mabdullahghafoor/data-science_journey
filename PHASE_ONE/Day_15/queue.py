# in this we will se how queue works in python

# ── Queue: First In, First Out (FIFO) ────────────────────────────
# Think of a queue at a bank:
# → First person in line = first person served
# → You ADD at the back (enqueue)
# → You REMOVE from the front (dequeue)

# Real world uses:
# → Print queue
# → Customer service ticket system
# → CPU task scheduling

from collections import deque   # efficient queue in Python!

class Queue:
    """Queue implementation using collections.deque."""

