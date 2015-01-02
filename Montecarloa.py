#!/usr/bin/env python3

import random
import math

darts = 10**6
hits = 0
throws = 0

for i in range (1,darts):
    throws = throws + 1
    x = random.random()
    y = random.random()
    dist = math.sqrt(x * x + y * y)
    #dist = math.sqrt(pow(x, 2) + pow(y, 2)) # modify this statement
     #because radius here is = to 1 it's possible to do more faster cancelled the math.sqrt()

    if dist <= 1.0:
        hits = hits + 1

pi = (hits/ throws) * 4

print('pi=', pi)
