import math
radius = float(raw_input("Radius (cm):"))
height = float(raw_input("Height (cm):"))

def volumed(r,h):
	v= math.pi*(r**2)*h
	return v
volume = volumed(radius,height)
def massed(v):
	m = v*22.59
	return m
mass = massed(volume)

print mass, "grams of Osmium will cost", mass*13, "dollars."