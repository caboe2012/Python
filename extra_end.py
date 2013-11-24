def extra_end(text):
	n = len(text)
	if n >= 2:
		first = text[n-2]
		last = text[n-1]
		new = first + last
		return 3 * new