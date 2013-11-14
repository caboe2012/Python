d = {
	"a" : "n", "A" : "N", "b" : "o", "B" : "O", "c" : "p", "C" : "P", "d" : "q", "D" : "Q", 
	"e" : "r", "E" : "R", "f" : "s", "F" : "S", "g" : "t", "G" : "T", "h" : "u", "H" : "U",
	"i" : "v", "I" : "V", "j" : "w", "J" : "W", "k" : "x", "K" : "X", "l" : "y", "L" : "Y",
	"m" : "z", "M" : "Z", "n" : "a", "N" : "A", "o" : "b", "O" : "B", "p" : "c", "P" : "C",
	"q" : "d", "Q" : "D", "r" : "e", "R" : "E", "s" : "f", "S" : "F", "t" : "g", "T" : "G",
	"u" : "h", "U" : "H", "v" : "i", "V" : "I", "w" : "j", "W" : "J", "x" : "k", "X" : "K",
	"y" : "l", "Y" : "L", "z" : "m", "Z" : "M", " ' " : " ' " 
}

def Rot13(sentence):
	l = []
	for each in sentence:
		if each.isalpha():
			new = d[each]
			l.append(new)
		else:
			l.append(each)
	print "".join(l)

user = raw_input("Enter a word or sentence to encrypt:")

print Rot13(user)