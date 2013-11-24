def combo_string(a,b):
	if len(a) > len(b):
		return b + a + b
	else:
		return a + b + a

print combo_string("hello", "hi")
print combo_string("hi", "hello")
print combo_string("aaa", "b")