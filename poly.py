#Draw a face

import turtle
import math

def draw_polygon(numSides, sideLength):
    angle = 360 / numSides
    for x in range(numSides):
        turtle.forward(sideLength)
        turtle.right(angle)

def draw_circle(radius):
    numSides = 360
    circumference = 2 * math.pi * radius
    sideLength = circumference / numSides
    draw_polygon(numSides, sideLength)

def draw_eye():
    draw_circle(20)
    turtle.color('blue')
    turtle.begin_fill()
    draw_circle(10)
    turtle.end_fill()



