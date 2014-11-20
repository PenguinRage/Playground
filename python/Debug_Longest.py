a = raw_input("first string? ")
b = raw_input("second string? ")
c = raw_input("third string? ")

longest = ""
if len(a) >= len(longest):
    longest = a
if len(b) > len(longest):
    longest = b
if len(c) > len(longest):
    longest = c

print "The longest line was:", longest