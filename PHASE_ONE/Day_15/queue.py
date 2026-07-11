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

    def dequeue(self):
        """Remove item from FRONT of queue — O(1)"""
        if self.is_empty():
            raise IndexError("Queue is empty!")
        item = self.__items.popleft()   # O(1) with deque!
        print(f"  Served: {item}")
        return item

    def front(self):
        """See who's next without removing."""
        if self.is_empty():
            raise IndexError("Queue is empty!")
        return self.__items[0]

    def is_empty(self):
        return len(self.__items) == 0

    def size(self):
        return len(self.__items)

    def __str__(self):
        return f"Queue: front → {list(self.__items)} ← back"

# ── Real Use: Bank Customer Service ──────────────────────────────
print("🏦 BANK CUSTOMER SERVICE SIMULATION")
print("─" * 40)

bank_queue = Queue()

# Customers arrive
customers = ["Ali", "Sara", "Fatima", "Omar", "Zara"]
for customer in customers:
    bank_queue.enqueue(customer)

print(f"\n{bank_queue}")
print(f"Next to be served: {bank_queue.front()}")
print(f"Waiting: {bank_queue.size()} customers\n")

# Serve customers one by one
print("Serving customers:")
while not bank_queue.is_empty():
    bank_queue.dequeue()
