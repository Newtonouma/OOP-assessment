class Rectangle:
    def __init__(self, length, width=None):
        # If only one argument is passed a square created
        if width is None:
            self.length = length
            self.width = length
        else:
            self.length = length
            self.width = width

    def area(self):
        return self.length * self.width

# Testing with a square
square = Rectangle(5)
print(f"Area of the square is {square.area()}")

# Test with a rectangle
rectangle = Rectangle(5, 10)
print(f"Area of the rectangle is {rectangle.area()}")
