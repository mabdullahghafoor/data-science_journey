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

    def size(self):
        return len(self.__items)

    def __str__(self):
        return f"Stack{self.__items} ← top"

# ── Using Stack ───────────────────────────────────────────────────
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack)            # Stack[10, 20, 30] ← top
print(f"Top: {stack.peek()}")   # 30
stack.pop()             # removes 30
stack.pop()             # removes 20
print(stack)            # Stack[10] ← top

# ── Real Use: Undo System ─────────────────────────────────────────
def text_editor_demo():
    """Simulate undo functionality using a stack."""
    text    = ""
    history = Stack()

    actions = ["Hello", " World", " Python", " Rocks"]

    for action in actions:
        text += action
        history.push(text)      # save state
        print(f"  Typed: '{text}'")

    print("\n  --- Undoing ---")
    while not history.is_empty():
        history.pop()
        if not history.is_empty():
            text = history.peek()
            print(f"  After undo: '{text}'")
        else:
            print("  After undo: ''")

text_editor_demo()

# ── Classic Problem: Balanced Brackets ───────────────────────────
def is_balanced(expression):
    """
    Check if brackets are balanced.
    '({[]})' → True
    '({[})' → False
    """
    stack   = Stack()
    opening = "({["
    closing = ")}]"
    pairs   = {")":"(", "}":"{", "]":"["}

    for char in expression:
        if char in opening:
            stack.push(char)
        elif char in closing:
            if stack.is_empty():
                return False
            if stack.pop() != pairs[char]:
                return False
