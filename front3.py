def front3(text):
	n = len(text)
	if n > 3:
		front = text[:3]
		return 3 * front
	else:
		return 3 * text