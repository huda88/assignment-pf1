import random
import math

def MontePi (num):
    inCircle= 0

    for _ in range (num):
        x = random.random()
        y = random.random()

        dist = math.sqrt( x ** 2 + y ** 2)

        if dist <= 1:
            inCircle = inCircle + 1

    pi = (inCircle/ num)*4

    return pi

