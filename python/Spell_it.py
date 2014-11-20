


def number2words(number):
	numberlist = {
	"0":'zero',
	"1":'one',
	"2":'two',
	"3":'three',
	"4":'four',
	"5":'five',
	"6":'six',
	"7":'seven',
	"8":'eight',
	"9":'nine',
	}
	n = str(number)
	numsen = ''
	for i in n:
		numsen += numberlist[i] + " "
	return numsen[:-1]
number2words(152)``