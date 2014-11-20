number = int(raw_input("Enter the length of the side: "))

def square(n):
	print "* "*(n-1) + "*"
	for i in xrange(1,n-1):
		print "* " + "  "*(n-2) + "*"
	print "* "*(n-1) + "*"
square(number)