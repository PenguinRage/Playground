number = raw_input("Enter the number:")

if int(number[-2:]) == 11 or int(number[-2:]) == 12 or int(number[-2:]) == 13:
	print number + "th"
elif int(number[-1]) == 1:
	print number + "st"
elif int(number[-1]) == 2:
	print number + "nd"
elif int(number[-1]) == 3:
	print number + "rd"
else:
	print number + "th"