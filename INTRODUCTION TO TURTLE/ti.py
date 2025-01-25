import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightblue")  # Background color of the screen

# Create a turtle object
pen = turtle.Turtle()
pen.speed(3)  # Set the drawing speed (1 - slowest, 10 - fastest)

# Function to draw an equilateral triangle
def draw_triangle():
    pen.penup()
    pen.goto(-200, 100)  # Position the turtle
    pen.pendown()
    pen.color("green")  # Set the color of the pen
    pen.begin_fill()  # Start filling the polygon
    for _ in range(3):
        pen.forward(200)  # Move the turtle forward by 200 units
        pen.left(120)  # Turn the turtle 120 degrees to the left
    pen.end_fill()  # End the filling of the polygon

# Function to draw a rectangle
def draw_rectangle():
    pen.penup()
    pen.goto(50, 100)  # Position the turtle
    pen.pendown()
    pen.color("red")  # Set the color of the pen
    pen.begin_fill()  # Start filling the polygon
    for _ in range(2):
        pen.forward(250)  # Move forward 250 units
        pen.left(90)
        pen.forward(100)  # Move forward 100 units
        pen.left(90)
    pen.end_fill()  # End the filling of the polygon

# Function to draw a hexagon
def draw_hexagon():
    pen.penup()
    pen.goto(-100, -150)  # Position the turtle
    pen.pendown()
    pen.color("purple")  # Set the color of the pen
    pen.begin_fill()  # Start filling the polygon
    for _ in range(6):
        pen.forward(100)  # Move forward 100 units
        pen.left(60)  # Turn the turtle 60 degrees to the left
    pen.end_fill()  # End the filling of the polygon

# Draw all shapes
draw_triangle()
draw_rectangle()
draw_hexagon()

# Hide the turtle and display the result
pen.hideturtle()

# Keep the window open until it is clicked
screen.exitonclick()
