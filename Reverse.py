def reverse(text):
    s = []
    t = []
    for each in text:
       s.append(each)
    counter = (len(s)-1)
    while counter >= 0:
        t.append(s[counter])
        counter -= 1
    for each in t:
        return "".join(t)
    print t

user = raw_input("Enter the word, phrase or number you'd like me to reverse: ")

print reverse(user)
print ("Ta dah!")