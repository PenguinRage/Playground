import re, Image

i = Image.open("oxygen.png") #openning image
print i
row = [i.getpixel((x,45)) for x in range(0, i.size[0], 7)]
ords = [r for r,g,b,a in row if r == g == b]

print "".join(map(chr,map(int, re.findall("\d+", "".join(map(chr, ords))))))
