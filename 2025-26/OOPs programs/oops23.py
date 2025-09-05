# Operator Overloading Create a Vector class that supports addition using the + operator, allowing you to add two vectors.



class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"


v1 = Vector(2, 4)
v2 = Vector(1, -1)
print("Vector Addition:", v1 + v2)