import math

class Ball(object):
	def __init__(self, color, radius):
		if radius <= 0:
			raise ValueError("Can't be less than or equal to 0")
		self.__color = color
		self.__radius = radius
		self.__diameter = 2 * radius 

	"""When calling color of ball or Radius."""
	def color(self):
		return self.__color

	def radius(self):
		return self.__radius

	def diameter(self):
 		return self.__diameter
	"""When Setting new values to radius or color"""
	def set_color(self, color):
		self.__color = color

	def set_radius(self, radius):
		if radius <= 0:
			raise ValueError("Can't be less than or equal to 0")
		self.__radius = radius
		self.__diameter = 2*radius

	def set_diameter(self, diameter):
		if diameter <= 0:
			raise ValueError("Can't be less than or equal to 0")
 		self.__diameter = diameter
 		self.__radius = diameter/2
 	
 	""" Making the new cases
 		Rule 1: Any type of output only really requires global variables and self"""

 	def circum(self):
 		return 2*math.pi*self.__radius

 	def volume(self):
 		return math.pi*self.__radius**2
 	
 	def descript(self):
 		print " The ball is: \n" + " color: " + self.__color + "\n" + " radius: " + str(self.__radius) + "\n" + " diameter: " + str(self.__diameter)
