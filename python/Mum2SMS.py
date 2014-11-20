import re
# Abbreviation search
fileHandler = open('C:\Users\Inc-Pro\Desktop\python\sms-phrases', 'rU').readlines()
abbr = []
meaning = []

# Splitting abreviation: LOL, Laughing out Loud
for x in fileHandler:
	meaning.append(x.split(' ',1)[0])
	abbr.append(x.split(' ',1)[1].replace('\n', ''))

# Searching entire message for 'patterns'
message = open('C:\Users\Inc-Pro\Desktop\python\mum-message', 'rU').read()
for c, i in enumerate(abbr):
	message = re.sub(meaning[c], meaning[c], message,flags=re.IGNORECASE)
	message = re.sub(i, meaning[c], message,flags=re.IGNORECASE)
print message