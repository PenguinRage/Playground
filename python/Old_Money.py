time = int(raw_input("Travel back in time to: "))
dollars = float(raw_input("2011 dollars: "))
def travel(t,d):
	times = 2011-t
	for i in range(0,times,1):
		d += d*(5.6/100)
	return d
print "In", time, "you would have", travel(time,dollars), "dollars of buying power."