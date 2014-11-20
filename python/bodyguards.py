import re

world = open('guards.txt', 'rU').read()
print "".join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", world))
