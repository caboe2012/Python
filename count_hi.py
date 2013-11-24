def count_hi(text):
	counter = 0
	for each in range(len(text)-1):
		if (text[each]) + (text[each+1]) == "hi":
			counter += 1
	return counter

print count_hi("hi there your hi ness! hi")