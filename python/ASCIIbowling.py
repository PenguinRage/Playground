num = int(raw_input("Length: "))
map = []
for x in range(num):
	line = ''
	for y in range (num):
		if y == x:
			line += 'O'
		else:
			line += '.'
	line += 'I'
	map.append(line)
map.append('.'*(num)+'X')
for i in map:
	print i
print 'Hit!'