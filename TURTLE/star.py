import turtle

# Set up the screen
screen = turtle.Screen()

# Create a turtle object
t = turtle.Turtle()

# Set the speed of the turtle
t.speed(3)

# Draw a star
for _ in range(5):
    t.forward(100)  # Move the turtle forward by 100 units
    t.right(144)    # Turn the turtle by 144 degrees to the right

# Hide the turtle after drawing
t.hideturtle()

# Keep the window open
turtle.done()
