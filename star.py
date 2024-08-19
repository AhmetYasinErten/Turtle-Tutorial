import turtle

drawing_board=turtle.Screen()
drawing_board.title("Star")
drawing_board.bgcolor("yellow")

point1=turtle.Turtle()
for i in range(5):
    point1.forward(300)
    point1.left(144)

turtle.done