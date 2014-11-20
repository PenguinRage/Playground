print "What is my favorite food?"
guess = ""
while guess != "electricity":
	guess = raw_input("Guess? ")
	if guess != "electricity":
		print "Not even close"
print "You guessed it! Buzzzz"