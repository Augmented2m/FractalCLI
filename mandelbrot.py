from simple_term_menu import *
import os

class Mandelbrot:

	def __init__(self):
		self.coords_xmin = -2
		self.coords_xmax = 1
		self.coords_ymin = -1
		self.coords_ymax = 1
		self.diff_x = 3
		self.diff_y = 2

		invalid = True
		while invalid:
			os.system('clear')
			resolutions = ["Custom resolution", "400 x 300", "800 x 600", "1200 x 900", "1600, 1200"]
			tm = TerminalMenu(resolutions, title="Resolution")
			r = tm.show()
			if not r == 0:
				self.width = (r)*400
				self.height = (r)*300
				invalid = False
			else:
				os.system('clear')
				try:
					self.width = int(input("Width: "))
					self.height = int(input("Height: "))
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
				self.iterations = iter_dic[r]
				invalid = False
			else:
				try:
					self.iterations = int(input("Iterations: "))
					invalid = False
				except ValueError:
					pass

		# colors (how many & which colors)
		os.system('clear')
