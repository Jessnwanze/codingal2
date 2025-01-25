import math

# Base class Polygon
class Polygon:
    def __init__(self):
        pass

    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Subclass for Rectangle
class Rectangle(Polygon):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Subclass for Triangle
class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Subclass for Circle
class Circle(Polygon):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# Subclass for Square (Special case of Rectangle)
class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

# Main program to test the classes
def main():
    # Create different polygon objects
    rectangle = Rectangle(10, 5)
    triangle = Triangle(6, 4)
    circle = Circle(7)
    square = Square(4)

    # Calculate and print the areas
    print(f"Area of Rectangle: {rectangle.area()} square units")
    print(f"Area of Triangle: {triangle.area()} square units")
    print(f"Area of Circle: {circle.area()} square units")
    print(f"Area of Square: {square.area()} square units")

# Run the main function
if __name__ == "__main__":
    main()
