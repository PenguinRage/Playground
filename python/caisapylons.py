number = int(raw_input())
pylons = raw_input().split()
energy,payment,count = 0,0,0

for i in pylons:
	while int(i) > energy:
		energy +=1
		payment+=1
		count+=1
	if energy > int(i):
		energy-=1
		count +=1
	if count > number:
		break;
print payment