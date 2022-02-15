Aaron Samaco
Phys 105A
#!/usr/bin/env python3
"""
computing pi using the Monte Carlo method.
"""
from random import random
from math import sqrt
# Number of random points:
N = 100
# of Counter of points inside:
I = 0
for i in range(N):
    # Generate random points in range [0,1)
    x = random()
    y = random()
    # Is it inside the circle?
    r = sqrt(x**2 + y**2)
    if r < 1: I += 1
# Calculate Pi: 
print(4 * I / N) 
