
lines = int(raw_input("Number of lines: "))
pattern = raw_input("Start line:")
print pattern
def patternmaker(p):
	newpattern = ""
	for c, i in enumerate(p):
		if c > 0 and c < len(p)-1:
			test = p[c-1] + p[c] + p[c+1] 
			if test in ("...", "***", ".*.", "*.*"):
				newpattern += "."
			elif test in ("**.", ".**", "..*", "*.."):
				newpattern += "*"
		# Wrap around cell
		elif c == 0:
			test = p[len(p)-1] + p[c] + p[c+1] 
			if test in ("...", "***", ".*.", "*.*"):
				newpattern += "."
			elif test in ("**.", ".**", "..*", "*.."):
				newpattern += "*"
		#last cell
		elif c == len(p)-1:
			test = p[c-1] + p[c] + p[0]
			if test in ("...", "***", ".*.", "*.*"):
				newpattern += "."
			elif test in ("**.", ".**", "..*", "*.."):
				newpattern += "*"
	return newpattern

for i in range(0,lines-1):
	pattern = patternmaker(pattern)
	print pattern

