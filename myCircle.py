import turtle
import math

turtle.clear()

#draw a circle function

turtle.speed(0)
pi= math.pi

def circle(rad):
    for i in range(0,36):
        turtle.forward(2*rad*pi/36)
        turtle.left(10)


# draw multicircle
        
def multicircle (n, rad):
    for i in range(n):
        circle(rad)
        turtle.right(360/n)
    
# general function for colored circle

def olympic (rad,x, y, width, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pensize(width)
    turtle.color(color)
    turtle.pendown()
    circle(rad)
    
# draw olympic circle

def 5olympic():    
	olympic(50, -125 , 0, 4, 'blue')
	olympic(50, 0, 0, 4, 'black')
	olympic(50, 125 , 0, 4, 'red')
	olympic(50, -62.5, -50, 4, 'yellow')
	olympic(50, 62.5, -50, 4, 'green')





