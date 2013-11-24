def end_other(a, b):
	c = a.lower()
	d = b.lower()
	if len(d) > len(c):
		if c == c[len(c)-1:len(d)]:
			return True
		else:
			return False
	elif len(d) < len(c):
		if d == c[len(d)-1:len(c)]:
			return True
		else:
			return False
	else:
		if len(d) == len(c):
			return True
		else:
			return False