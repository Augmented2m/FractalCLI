from simple_term_menu import *
import os

class Sierpinski:

	def __init__(self):
		print("Sierpinski")

	
#!/usr/bin/python3

import random
import matplotlib.pyplot as plt
import time

t0 = time.time()

class Punkt():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, x2):
        r = Punkt(self.x + x2.x, self.y + x2.y)
        return r
    def __sub__(self, x2):
        r = Punkt(self.x - x2.x, self.y - x2.y)
        return r
    def __mul__(self, x2):
        r = Punkt(self.x * x2, self.y * x2)
        return r
    def print(self):
        print(self.x, self.y)

def algorythmus(p):
    for i in range(number):
        p = p + (random.choice([A, B, C]) - p) * 0.5
        plot_x.append(p.x)
        plot_y.append(p.y)


A = Punkt(0, 0)
B = Punkt(2, 0)
C = Punkt(1, 2)
p = Punkt(random.randint(-100, 100), random.randint(-100, 100))
number = 100000
plot_x = []
plot_y = []
plt.axis([0, 2, 0, 2])
algorythmus(p)
plt.plot(plot_x, plot_y, "bo")

print(time.time() - t0)
plt.show()
