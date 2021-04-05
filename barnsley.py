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

        def translate(value, leftMin, leftMax, rightMin, rightMax):
            leftSpan = leftMax - leftMin
            rightSpan = rightMax - rightMin
            valueScaled = float(value - leftMin) / float(leftSpan)
            return rightMin + (valueScaled * rightSpan)


        width = 5000
        height = 5000

        img = Image.new('RGB', (width, height), color = 'white')
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

        img.save("test.png")
        #plt.scatter(px, py, color='green', s=0.1)
        #plt.show()
