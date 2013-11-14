def anti_vowel(text):
    s=[]
    if len(text) > 0:
        i = 0
        for each in user:
            if each in "aeiouAEIOU":
                i += 1
                print i
            else:
                s.append(each)
        print ("there are %i vowels in your word." %i)
        print ",".join(s)
    else:
        print "You didn't enter anything!"

user = raw_input('Enter a word:')

print anti_vowel(user)
