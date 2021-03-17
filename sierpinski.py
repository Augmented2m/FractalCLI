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
		os.system('clear')
		
		self.width = 8000
		self.height = 8000
		self.img = Image.new('RGB', (self.width, self.height), color = 'white')
		self.pixels = self.img.load()

		self.A = Punkt(0, 0)
		self.B = Punkt(self.width, 0)
		self.C = Punkt(self.width/2, self.height)
		p = Punkt(random.randint(0, self.width), random.randint(0, self.height))
		self.number = 1000000000
		self.algorithm(p)
		self.img.save('output.png')

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


