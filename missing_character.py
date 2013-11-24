def missing_char(text, n):
	a = text[:n]
	b = text[n+1:]

	return a + b

print missing_char("kitten", 4)
