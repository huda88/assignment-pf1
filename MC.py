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
    dist = x ** 2 + y ** 2

    if dist <= 1:
        hits = hits + 1

pi = (hits/ throws) * 4

print('pi=', pi)
