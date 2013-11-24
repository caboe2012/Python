def cat_dog(text):
	cat = 0
	dog = 0
	for each in range(len(text)-2):
			if text[each] + text[each+1] + text[each+2] == "cat":
				cat += 1
			elif text[each] + text[each+1] + text[each+2] == "dog":
				dog += 1
	if cat == dog:
		return True
	else:
		return False
