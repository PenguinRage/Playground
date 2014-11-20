import string

original = "http://www.pythonchallenge.com/pc/def/map.html"

table = string.maketrans(
    "abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab"
)

print original.translate(table)