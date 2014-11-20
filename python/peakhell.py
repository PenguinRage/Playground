import urllib, pickle

source = urllib.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
data = pickle.load(source)
source.close()

for elt in data:
	print "".join([e[1] * e[0] for e in elt]) #list comprehension