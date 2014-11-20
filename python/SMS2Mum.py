
# Abbreviation search
fileHandler = open('C:\Users\Inc-Pro\Desktop\python\sms-phrases', 'rU').readlines()
abbr = []
meaning = []


# Splitting abreviation: LOL, Laughing out Loud
for x in fileHandler:
	abbr.append(x.split(' ',1)[0])
	meaning.append(x.split(' ',1)[1].replace('\n', ''))
	define = {}

# Creating abbreviation Dictionary
for c, word in enumerate(abbr):
	define[word] = meaning[c]
	print define[word].lower()

# Reading message by line
message = open('C:\Users\Inc-Pro\Desktop\python\sms-message', 'rU')

#Beginning
line = message.readline().split()
print line
for c, word in enumerate(line):
	words = word.replace(",", "").upper() 
	if words in define:
		line[c] = define[words]
		if "," in word:
				line[c] += ","
print ' '.join(line)

#Middle
while line:
	line = message.readline().split()
	for c, word in enumerate(line):
		words = word.replace(",", "").upper()
		if words in define:
			line[c] = define[words]
			if "," in word:
				line[c] += ","
	print ' '.join(line)

#End
line = message.readline().split()
for c, word in enumerate(line):
	words = word.replace(",", "").upper()
	if words in define:
		line[c] = define[words]
		if "," in word:
				line[c] += ","
print ' '.join(line)
