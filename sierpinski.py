import colorsys
from simple_term_menu import *
import os
import random
import matplotlib.pyplot as plt
import time
from tqdm import tqdm
from PIL import Image

class Sierpinski:

    def __init__(self):
        invalid = True
        while invalid:
            os.system('clear')
            resolutions = ["Custom resolution", "400 x 400", "800 x 800", "1200 x 1200", "1600 x 1600"]
            tm = TerminalMenu(resolutions, title="Resolution")
            r = tm.show()
            if not r == 0:
                self.width = (r)*400
                self.height = self.width
                invalid = False
            else:
                os.system('clear')
                try:
                    self.width = int(input("Resolution (width = height): "))
                    self.height = self.width
                    invalid = False
                except ValueError:
                    pass

        invalid = True
        while invalid:
            os.system('clear')
            numbers = ["Custom iterations", "10.000", "100.000", "1.000.000", "10.000.000"]
            tm = TerminalMenu(numbers, title="Iterations")
            r = tm.show()
            if not r == 0:
                self.number = 10**(r+3)
                invalid = False
            else:
                os.system('clear')
                try:
                    self.number = int(input("Iterations: "))
                    invalid = False
                except ValueError:
                    pass

        os.system('clear')
        self.name = input('Enter the name of the image: ')
        os.system('clear')

        self.img = Image.new('RGB', (self.width, self.height), color = 'white')
        self.pixels = self.img.load()

        self.A = Punkt(0, 0)
        self.B = Punkt(self.width, 0)
        self.C = Punkt(self.width/2, self.height)
        p = Punkt(random.randint(0, self.width), random.randint(0, self.height))
        self.algorithm(p)
        self.img.save(self.name + '.png')

    def algorithm(self, p):
        for i in tqdm(range(self.number)):
            p = p + (random.choice([self.A, self.B, self.C]) - p) * 0.5
            self.pixels[p.x,-p.y] = (0, 0, 0)


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
