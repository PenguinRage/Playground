import os

doc = open('rarechar.txt', 'rU')
letters = doc.read()
results = {}

for i in letters:
	if i not in results:
		results[i] = 1
	else:
		results[i] += 1
sentence =''
for i in results:
	if results[i] == 1:
		sentence += i
print sorted(sentence)