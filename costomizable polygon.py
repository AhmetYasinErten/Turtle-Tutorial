import turtle
inp=int(input("kenar sayısı giriniz:"))
angle=360/inp

draw_board=turtle.Screen()
turtle.bgcolor("light blue")
turtle.title("costomizable polygon")

point=turtle.Turtle()
for i in range (inp):
    point.forward(1600/inp)
    point.left(angle)
turtle.done