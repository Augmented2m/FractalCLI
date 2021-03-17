from simple_term_menu import *
import os

class Julia:

	def __init__(self):
		# coords may incorrect
		self.coords_xmin = -2
		self.coords_xmax = 2
		self.coords_ymin = -1
		self.coords_ymax = 1
		self.diff_x = 2
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

		print("Julia")
		print(self.width)
		print(self.height)
