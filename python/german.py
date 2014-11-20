"""
   ___   __  __            _        __ 
  / _ \ /__\/__\  /\/\    /_\    /\ \ \
 / /_\//_\ / \// /    \  //_\\  /  \/ /
/ /_\\//__/ _  \/ /\/\ \/  _  \/ /\  / 
\____/\__/\/ \_/\/    \/\_/ \_/\_\ \/  
                                       
"""

NUMBERS = {
  0: 'null', 1: 'eins', 2: 'zwei', 3: 'drei', 4: 'vier', 
  5: 'fuenf', 6: 'sechs', 7: 'sieben', 8: 'acht', 9: 'neun', 10: 'zehn',
  11: 'elf', 12: 'zwoelf', 13: 'dreizehn', 14: 'vierzehn', 15: 'fuenfzehn', 
  16: 'sechzehn', 17: 'siebzehn', 18: 'achtzehn', 19: 'neunzehn',
  20: 'zwanzig', 30: 'dreissig', 40: 'vierzig', 50: 'fuenfzig', 60: 'sechzig', 
  70: 'seibzig', 80: 'achtzig', 90: 'neunzig', 100: 'hundert', 1000: 'tausend',
}
ABBREV = {1: 'ein', 6: 'sech', 7: 'seib'}

def num2german(num):
	if num < 100:
		return lessthanhund(num)
	elif num >= 100 and num < 1000:
		return hundredrunner(num)
	elif  num > 999 and num < 10000:
		return thousandrunner(num)

def thousandrunner(num):
	remainder = num % 1000
	thousands = (num - remainder)/1000
	if remainder != 0:
		if thousands == 1 or thousands == 6 or thousands == 7:
			return ABBREV[thousands] + NUMBERS[1000] + hundredrunner(remainder)
		else:
			return NUMBERS[thousands] + NUMBERS[1000] + hundredrunner(remainder)
	else:
		if thousands == 1 or thousands == 6 or thousands == 7:
			return ABBREV[thousands] + NUMBERS[1000]
		else:
			return NUMBERS[thousands] + NUMBERS[1000]

def hundredrunner(num):
	remainder = num % 100
	hundreds = (num - remainder)/100
	if remainder != 0:
		if hundreds == 1 or hundreds == 6 or hundreds == 7:
			return ABBREV[hundreds] + NUMBERS[100] + lessthanhund(remainder)
		else:
			return NUMBERS[hundreds] + NUMBERS[100] + lessthanhund(remainder)
	else:
		if hundreds == 1 or hundreds == 6 or hundreds == 7:
			return ABBREV[hundreds] + NUMBERS[100]
		else:	
			return NUMBERS[hundreds] + NUMBERS[100]

def lessthanhund(num):
  if num < 20: # Counting Cases up to twenty
  	return NUMBERS[num]
  elif num >= 20 and num % 10 == 0 and num < 100: # Counting cases by 10s, less than 100
  	return NUMBERS[num]
  elif num >= 20 and num % 10 != 0 and num < 100: #Counting cases for the remainder within 100
  	remainder = num % 10
  	return NUMBERS[remainder] + 'und' + NUMBERS[num - remainder]
  return 'german'

