import urllib, re, time

uri = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s" 
nothing_rep = "and the next nothing is (\d+)"
nothing = "8022" #You'll later be asked to divide by two"

while True:
	try:
		source = urllib.urlopen(uri % nothing).read()
		nothing = re.search(nothing_rep, source).group(1)
	except: 
		break
	
	print nothing
print source