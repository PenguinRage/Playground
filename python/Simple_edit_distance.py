worda = raw_input("Word 1: ")
wordb = raw_input("Word 2: ")
count = 0
for c, i in enumerate(worda):
	if i != wordb[c]:
		count +=1
print count