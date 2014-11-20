home = raw_input("Team 1: ")
away = raw_input("Team 2: ")

if len(home) > len(away):
	print home
elif len(home) < len(away):
	print away
else:
	print "Draw"