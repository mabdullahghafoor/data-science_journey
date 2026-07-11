# in this we will se how stack works in python

# ── Stack: Last In, First Out (LIFO) ─────────────────────────────
# Think of a stack of plates:
# → You ADD to the top (push)
# → You REMOVE from the top (pop)
# → Last plate placed = First plate removed

# Real world uses:
# → Undo/Redo in text editors
# → Browser back button
# → Function call stack in Python itself!

class Stack:
    """Stack implementation using a list."""

    def __init__(self):
        self.__items = []       # private internal list

    def push(self, item):
        """Add item to top of stack — O(1)"""
        self.__items.append(item)
        print(f"  Pushed: {item}")

    def pop(self):
        """Remove and return top item — O(1)"""
        if self.is_empty():
            raise IndexError("Stack is empty!")
        item = self.__items.pop()
        print(f"  Popped: {item}")
        return item

    def peek(self):
        """See top item without removing — O(1)"""
        if self.is_empty():
            raise IndexError("Stack is empty!")
        return self.__items[-1]

    def is_empty(self):
        return len(self.__items) == 0

