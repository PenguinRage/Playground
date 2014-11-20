import math

rad = float(raw_input("Radius: "))

def egypt(r):
	area = (64*((2*r) ** 2))/81
	return area

def pie(r):
	area = math.pi*r**2
	return area

print "Egyptian area =", egypt(rad)
print "Real area =", pie(rad)