from PIL import Image
import colorsys
import math
import os
from simple_term_menu import *
import os
from tqdm import tqdm

class Julia:

    def __init__(self):
        invalid = True
        while invalid:
            os.system('clear')
            resolutions = ["Custom resolution", "400 x 300", "800 x 600", "1200 x 900", "1600 x 1200"]
            tm = TerminalMenu(resolutions, title="Resolution")
            r = tm.show()
            if not r == 0:
                self.width = (r)*400
                self.height = (r)*300
                self.aspectRatio = 4/3 
                invalid = False
            else:
                os.system('clear')
                try:
                    self.width = int(input("Width: "))
                    self.height = int(input("Height: "))
                    self.aspectRatio = self.width/self.height 
                    invalid = False
                except ValueError:
                    pass

        invalid = True
        while invalid:
            os.system('clear')
            iterations = ["Custom iterations", "100", "250", "500", "750", "1000"]
            iter_dic = {1:100, 2:250, 3:500, 4:750, 5:1000}
            tm = TerminalMenu(iterations, title="Iterations")
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

        # colors (how many & which colors)
        os.system('clear')

        x = -0.65
        y = 0
#        self.xRange = 3.4
#        self.yRange = self.xRange / self.aspectRatio
        self.minX = -1.5
        self.maxX = 1.5
        self.minY = -1.5
        self.maxY = 1.5

        self.xRange = 3
        self.yRange = 3
        
        self.img = Image.new('RGB', (self.width, self.height), color = 'black')
        self.pixels = self.img.load()

        self.algorithm()

        self.img.save('output.png')

    def algorithm(self):
        cx, cy = -0.1, 0.65

        for row in tqdm(range(self.height)):
            for col in range(self.width):
                zx = self.minX + col * self.xRange / self.width
                zy = self.maxY - row * self.yRange / self.height

                i = 0
                
                while zx*zx + zy*zy < 10 and i < self.precision:
                    xtmp = zx*zx - zy*zy
                    zy = 2*zx*zy + cy
                    zx = xtmp + cx

                    i += 1

                if i < self.precision:
                    distance = (i + 1) / (self.precision + 1)
                    rgb = self.powerColor(distance, 0.2, 0.27, 1.0)
                    self.pixels[col,row] = rgb


    def logColor(self, distance, base, const, scale):
        color = -1 * math.log(distance, base)
        rgb = colorsys.hsv_to_rgb(const + scale * color,0.8,0.9)
        return tuple(round(i * 255) for i in rgb)
    
    def powerColor(self, distance, exp, const, scale):
        color = distance**exp
        rgb = colorsys.hsv_to_rgb(const + scale * color,1 - 0.6 * color,0.9)
        return tuple(round(i * 255) for i in rgb)
    
