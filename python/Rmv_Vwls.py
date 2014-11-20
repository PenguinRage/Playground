test = raw_input("Write a sentence:")

def remove_vowels(s):
	sentence = ""
 	for x in s:
 		X = x.lower()
 		if X not in ('a', 'i', 'e', 'o', 'u'):
 			sentence += x
 	return sentence

print remove_vowels(test)