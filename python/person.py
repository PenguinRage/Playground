class Person(object):
	def __init__(self,fname, lname):

Experimenting with raising Exceptions

		"""fname = fname.strip()
		if not fname:
			raise ValueError("The first name can't be blank")
		lname = lname.strip()
		if not lname:
			raise ValueError("The last name can't be blank")"""

		self.__fname = fname
		self.__lname = lname
	
	def fname(self):
		return self.__fname

	def set_fname(self, fname):
		fname = fname.strip()
		if not fname:
			raise ValueError("The first name can't be blank")
		self.__fname = fname
	
	def lname(self):
		return self.__lname

	def set_lname(self, lname):
		lname = lname.strip()
		if not lname:
			raise ValueError("The last name can't be blank")
			self.__lname = lname

	def name(self):
		return self.__fname + ' ' + self.__lname

