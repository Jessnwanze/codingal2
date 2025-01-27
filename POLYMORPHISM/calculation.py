from math import pi

# Base class: Polygon
class Polygon:
    def area(self):
        raise NotImplementedError("This method should be overridden by subclasses")

# Derived class: Rectangle
class Rectangle(Polygon):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Derived class: Circle
class Circle(Polygon):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

# Derived class: Triangle
class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Function to test the program
def main():
    # Creating instances of each polygon
    rectangle = Rectangle(10, 5)
    circle = Circle(7)
    triangle = Triangle(6, 4)

    # Displaying the areas
    print("Area of Rectangle:", rectangle.area())
    print("Area of Circle:", circle.area())
    print("Area of Triangle:", triangle.area())

if __name__ == "__main__":
    main()
