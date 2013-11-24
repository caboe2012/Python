def double_char(text):
	n = len(text)
	i = 0 
	l = []
	while i <= n-1:
		l.append(2 * text[i])
		i += 1
	return "".join(l)

double_char("practice")




def double_char_simple(text):
	s= ""
	for i in range(len(text)):
		s += text[i] + text[i]
	return s

print double_char_simple("hey there Rachel!")