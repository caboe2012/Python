def diff21(n):
	if n <= 21:
		t = abs(n-21)
		return t
	else:
		t = 2 * (abs(n-21))
		return t

print diff21(-100)