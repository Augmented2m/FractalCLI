from simple_term_menu import *
from mandelbrot import Mandelbrot
from julia import Julia
from sierpinski import Sierpinski
from barnsley import Barnsley
import os
from ascii_magic import from_image_file

def show_image_w(x):
    p = x+'.png'
    if p in os.listdir():
        return str(image.Image(p))
    else:
        return "No preview available"

def show_image(x):
    p = x+'.png'
    if p in os.listdir():
        return str(from_image_file(p, columns=90))
    else:
        return "No preview available"

def main():
    os.system('clear')
    fractals = ["Mandelbrot-Menge", "Julia-Menge", "Sierpinski Dreieck", "Barnsley"]
    fractal_class = {0: Mandelbrot, 1: Julia, 2: Sierpinski, 3: Barnsley}
    fractal_menu = TerminalMenu(fractals, preview_command=show_image, preview_size=0.9, title="Fractal")
    chosen_fractal = fractal_menu.show()
    fractal_class[chosen_fractal]()

if __name__=="__main__":
    main()
