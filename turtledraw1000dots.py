import turtle
import random

turtle.speed(0)
turtle.pensize(3)

#one thousand dot on turtle:

def drawdot ():
    for i in range(1000):
        #choose a random point in the screen
        x = random.randint(-150,150)
        y = random.randint(-150,150)

        #go to the coordinate x, y in the screen
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        turtle.dot()

#draw 1000 dot 2 color
        
def drawdot2 ():
    for i in range(1000):
        color= ['blue', 'red', 'yellow', 'green']
        k= random.randint(0,3)
        turtle.color(color[k])
        #choose a random point in the screen
        x = random.randint(-150,150)
        y = random.randint(-150,150)

        #go to the coordinate x, y in the screen
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        turtle.dot()

