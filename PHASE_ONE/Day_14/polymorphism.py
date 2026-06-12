# In this we will see how we can use polymorphism

# ── Polymorphism: same method name, different behavior ────────────
# "poly" = many, "morph" = form

class Shape:
    def area(self):
        return 0

    def describe(self):
        print(f"I am a {type(self).__name__} "
              f"with area {self.area():.2f}")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):                         # overrides parent
        return 3.14159 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width  = width
        self.height = height

    def area(self):                         # overrides parent
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base   = base
        self.height = height
