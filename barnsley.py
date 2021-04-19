import matplotlib.pyplot as plt
import random
import colorsys
from simple_term_menu import *
import os
import time
from tqdm import tqdm
from PIL import Image

class Barnsley:

    def __init__(self):

        invalid = True
        while invalid:
            os.system('clear')
            resolutions = ["Custom resolution", "400 x 400", "800 x 800", "1200 x 1200", "1600 x 1600"]
            tm = TerminalMenu(resolutions, title = "Resolution")
            r = tm.show()
            if not r == 0:
                self.resolution = (r)*400
                invalid = False
            else:
                os.system('clear')
                try:
                    self.resolution = int(input("Resolution: "))
                    invalid = False
                except ValueError:
                    pass

        invalid = True
        while invalid:
            os.system('clear')
            iterations = ["Custom iterations", "100", "250", "500", "750", "1000"]
            iter_dic = {1:100, 2:250, 3:500, 4:750, 5:1000}
            r = tm.show()
            if not r == 0:
                self.precision = iter_dic[r]
                invalid = False
            else:
                try:
                    self.precision = int(input("Iterations: "))
                    invalid = False
                except ValueError:
                    pass

        os.system('clear')

        self.name = input("Enter the name of your image: ")

        os.system('clear')
            

        def translate(value, leftMin, leftMax, rightMin, rightMax):
            leftSpan = leftMax - leftMin
            rightSpan = rightMax - rightMin
            valueScaled = float(value - leftMin) / float(leftSpan)
            return rightMin + (valueScaled * rightSpan)


        img = Image.new('RGB', (resolution, resolution), color = 'white')
        pixels = img.load()

        px, py = [], []

        x, y = 0, 0
        nx, ny = x, y

        for i in tqdm(range(10000000)):
            px.append(nx)
            py.append(ny)

            r = random.random()
            if r<0.01:
                nx = 0
                ny = 0.16*ny
            elif r<0.86:
                nx = 0.85*nx + 0.04*ny
                ny = -0.04*nx + 0.85*ny + 1.6
            elif r<0.93:
                nx = 0.2*nx - 0.26*ny
                ny = 0.23*nx + 0.22*ny + 1.6
            else:
                nx = -0.15*nx + 0.28*ny
                ny = 0.26*nx + 0.24*ny + 0.44

        xm = min(px)
        ym = min(py)
        xma = max(px)
        yma = max(py)

        for i in range(len(px)):
            pixels[int(translate(px[i], xm, xma, 1, width-1)),int(translate(py[i], ym, yma, height-1, 1))] =(0,255,0)

        img.save(self.name + ".png")
        #plt.scatter(px, py, color='green', s=0.1)
        #plt.show()
