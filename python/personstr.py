class Person(object):

	def __str__(self):
		return self.__fname + ' ' + self.__lname
		self.__fname = fname
		self.__lname = lname
	
	def fname(self):
		return self.__fname

	def lname(self):
		return self.__lname