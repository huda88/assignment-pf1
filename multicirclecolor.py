import turtle
import random

import math
turtle.pensize(5)
turtle.speed(0)
pi= math.pi

def circle(rad):
    for i in range(0,36):
        turtle.forward(2*rad*pi/36)
        turtle.left(10)
        
# 3 color
def multicircle3 (n, rad):
    k=0
    for i in range(n):
        if k<=2:
            color=['blue','red', 'green']
            turtle.color(color[k])
            circle(rad)
            turtle.right(360/n)
            k+=1
        else:
            k=0
            color=['blue','red', 'green']
            turtle.color(color[k])
            circle(rad)
            turtle.right(360/n)
            k+=1
            
#circle multi or more color

def multicircle_m (n, rad):
    for i in range(n):
        r=random.random()
        g=random.random()
        b=random.random()
        turtle.color(r,g,b)
        circle(rad)
        turtle.right(360/n)
