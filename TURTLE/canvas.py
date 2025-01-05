import turtle

# creating canvas
turtle.screen().bgcolor("yellow")

sc = turtle.screen()
sc.setup(400, 300)

turtle.title("Welcome to Turtle Window")

#turtle object creation
board = turtle.turtle()

# creating a square
for i in range(4):
    board.forward(100)
    board.left(90)
    i = i + 1