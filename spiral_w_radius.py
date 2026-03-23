import turtle
import math
a = int(input("initial side: .... "))
angle = int(input("Angle: ... "))
angle1 = angle
l = int(input("Iterations: ... "))
wn = turtle.Screen()
wn.delay(1)
tess = turtle.Turtle()
tess.color("DarkBlue")
tess.speed(10)
tess.up()
tess.forward(a)
tess.down()
tess.left(90)
trt = turtle.Turtle()
trt.color("LightGrey")
trt.forward(a)
trt.goto(0,0)
for i in range(l):
    c = a / math.cos(math.radians(angle))
    b = c * math.sin(math.radians(angle))
    tess.forward(b)
    tess.left(angle)
    trt.left(angle)
    trt.forward(0.999*c)
    trt.write(i)               # writes node #
    trt.goto(0,0)
    a = c
    


wn.exitonclick()
