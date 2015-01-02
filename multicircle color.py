import random
import turtle
turtle.speed(0)

def drawdot (rad):
    for i in range(50):
        #choose a random point in the screen
        x = random.randint(-200,200)
        y = random.randint(-200,200)
        #go to the coordinate x, y in the screen
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        r=random.random()
        g=random.random()
        b=random.random()
        turtle.fillcolor(r,g,b)
        turtle.begin_fill()
        turtle.circle(rad)
        turtle.end_fill()
