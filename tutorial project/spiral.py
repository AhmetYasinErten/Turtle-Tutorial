import turtle
from random import randint
color_list=["red","blue","green","purple","yellow","orange","gray"]
draw_board=turtle.Screen()
turtle.title("spiral")
turtle.bgcolor("yellow")

point=turtle.Turtle()

for i in range(20):
    point.color(color_list[i%7])
    point.circle(10*i)
    point.circle(-10*i)
    point.left(i)

turtle.mainloop()
