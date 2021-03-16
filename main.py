from simple_term_menu import *

def main():
    fractals = ["Mandelbrot-Menge", "Julia-Menge", "Sierpinski Dreieck"]
    fractal_menu = TerminalMenu(fractals, title="Fractal")
    chosen_fractal = fractal_menu.show()
    print(chosen_fractal)


if __name__=="__main__":
    main()
