import random
import turtle
import math

turtle.speed(0)
turtle.pensize(3)

#circle function

turtle.speed(0)
pi= math.pi

def circle(rad):
    for i in range(0,36):
        turtle.forward(2*rad*pi/36)
        turtle.left(10)

#draw cartesian line

def drawflechette():
    turtle.penup()
    turtle.goto(-200,0)
    turtle.pendown()
    turtle.goto(200,0)
    turtle.penup()
    turtle.goto(0,200)
    turtle.right(90)
    turtle.down()
    turtle.goto(0,-200)
    turtle.penup()
    turtle.goto(-200,15)
    turtle.pendown()
    circle(200)



#draw dot in the table

def drawdot (a):
    blue= 0
    yellow= 0
    green= 0
    brown= 0
    for i in range(a):
        #choose a random point in the screen
        x = random.randint(-200,200)
        y = random.randint(-200,200)

        #go to the coordinate x, y in the screen
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        dist=(x - 0) ** 2 + (y - 0) ** 2
        # draw for every cartesian  sector in a different color
        if dist <= 200**2:
            if x < 0 and y < 0:
                turtle.color('blue')
                turtle.dot()
                blue += 1
            elif x < 0 and y > 0:
                turtle.color('yellow')
                turtle.dot()
                yellow += 1
            elif x >=0 and y >= 0:
                turtle.color('green')
                turtle.dot()
                green +=1
            else:
                turtle.color('brown')
                turtle.dot()
                brown +=1
        else:
            turtle.color('red')
            turtle.dot()

    print('Quadrant 1:',blue,'Quadrant 2:',yellow,'Quadrant 3:',green,'Quadrant 4:',brown)

drawflechette()
drawdot(30)

