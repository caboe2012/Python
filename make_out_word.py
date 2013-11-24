def make_out_word(a, b):
	front = a[0:2] # example: CHAD -> CH (returns letters 1 and 2, 0 to n-1)
	back = a[3:5] # example: CHAD -> AD (returns letters 3 and 4)
	return front + b + back