import re

race = raw_input("Enter:")
sentence = race.split()

star = re.findall(r"s *t *a *r", race.strip().lower()) 
shell = re.findall(r"s *h *e *l *l", race.strip().lower())
	
if len(star) > len(shell) and len(star) > 0:
	print 'INVINCIBLLLLE!'
elif len(shell) > len(star):
	print 'CRASH!'
else:
	print 'Just drive.'
