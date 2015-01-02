import ant
import turtle
import random

turtle.setworldcoordinates(-10, -10, 310, 310) 

turtle.speed(0)

#draw the square

for i in range(4):
    turtle.forward(300)
    turtle.left(90)

def checkAntTell(x,y):
    ant.tell(x,y)
    if 0 <= x <= 300:
        if 0 <= y <= 300:
            return 1
    else:
        return 0


for i in range(3000):
    x= random.randint(-300,400)
    y= random.randint(-200,400)
    a= ant.tell(x,y)
    if checkAntTell(x,y) == 1:
        turtle.penup()
        turtle.goto(x,y)
        #pensize for the probability
        pensize= int(a*10)
        turtle.pensize(pensize)
        c= round(a,2)
        r= round( c/7,2)
        g= round(c/1.2,2)
        b= round(c/1.5,2)
        turtle.pencolor(r,g,b)
        turtle.dot()
    else:
        checkAntTell(x,y) == 0
