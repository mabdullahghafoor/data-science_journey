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

    def __init__(self):
        self.__items = deque()  # deque is faster than list for queue

    def enqueue(self, item):
        """Add item to BACK of queue — O(1)"""
        self.__items.append(item)
        print(f"  Joined queue: {item}")
