def front_back(text):
	n = len(text)
	if n > 2:
		first = text[0]
		last = text[n-1]
		middle = text[1:n-1] # can also write text[1:-1]
		return last + middle + first
	elif n == 2:
		first = text[0]
		last = text[1]
		return last + first
	else:
		return text

print front_back("table")
print front_back("cad")
print front_back("bottle")