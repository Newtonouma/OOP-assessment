class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Operand must be of type 'Vector'")

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

vector1 = Vector(3, 4)
vector2 = Vector(1, 2)

result = vector1 + vector2

print(f"Result of adding {vector1} and {vector2}: {result}")
