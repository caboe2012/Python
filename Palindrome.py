def reverse(words):
    s = []
    i = 0
    while i < len(words):
        s.append(words[i])
        i += 1
    print s
    l = []
    counter = (len(words) -1)
    while counter > -1:
        l.append(words[counter])
        counter -= 1
    print l
    if s == l:
        print "Cool! " + words.upper() + " is a Palindrome!"
    else:
        print "Hate to break it to you my friends but " + words.upper() + " isn't a Palindrome."  

user = raw_input("Enter a word that I may check it's palindrominess: ")

print reverse(user)