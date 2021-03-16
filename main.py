from simple_term_menu import *
from mandelbrot import Mandelbrot
from julia import Julia
from sierpinski import Sierpinski
import os

def main():
	os.system('clear')
	fractals = ["Mandelbrot-Menge", "Julia-Menge", "Sierpinski Dreieck"]
	fractal_class = {0: Mandelbrot, 1: Julia, 2: Sierpinski}
	fractal_menu = TerminalMenu(fractals, title="Fractal")
	chosen_fractal = fractal_menu.show()
	fractal_class[chosen_fractal]()

if __name__=="__main__":
	main()
