import  turtle

# draw a nuclear symbol (not finish)

def square(l):
    for i in range(4):
        turtle.forward(l)
        turtle.right(90)

def triangle (l):
    for i in range(3):
        turtle.color('black', 'black')
        turtle.begin_fill()
        turtle.right(120)
        turtle.forward(l/2-10)
        turtle.left(90)
        turtle.circle(l/2-5, 60)
        turtle.left(90)
        turtle.forward(l/2-10)
        turtle.left(120)
        turtle.end_fill()

turtle.clear()
turtle.color('black')
turtle.penup()
turtle.goto(-200,200)
turtle.pensize(5)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor('yellow')
square(200)
turtle.end_fill()
turtle.penup()
turtle.goto(-100,100)
turtle.pendown()

triangle(200)

turtle.goto(-98, 85 )
turtle.color('yellow', 'black')
turtle.begin_fill()
turtle.circle(14)
turtle.end_fill()
