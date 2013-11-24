def not_string1(text):
	if "not" in text:
		return text
	else:
		return ("not " + text)


def not_string2(text):
	if text[0] == "n" and text[1] == "o" and text[2] == "t":
		return text
	else:
		return ("not " + text)

print not_string("not bad")



def not_string3(text):
	if len(text) >= 3 and text[:3] == "not":
		return text
	else:
		return ("not " + text)

print not_string3("come get some!")