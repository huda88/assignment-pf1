import turtle
import math

turtle.speed(0)


def draw_shape ( w, angle, a):
    for i in range(a):
        turtle.forward(w)
        turtle.right(angle)

# draw an hexagon
draw_shape(20 ,60 , 6)
    
turtle.clear()

#draw a circle with shape

draw_shape(1,1,360)

turtle.clear()

#draw a cirlce

turtle.circle(4)


#circle and location

turtle.penup()
turtle.goto(45,52)
turtle.pendown()
turtle.circle(40)

turtle.clear()

#draw a graph

turtle.setworldcoordinates(-30, -2, 30, 200)

def parab(x):
    for i in range (x):
        turtle.penup()
        turtle.goto(i,i**2)
        turtle.dot()
    for i in range(x):
        turtle.penup()
        turtle.goto(-i,i**2)
        turtle.dot()

parab(20)


#draw a circle function

turtle.speed(0)
pi= math.pi

def circle(rad):
    for i in range(0,36):
        turtle.left(360/rad)

circle(100)
