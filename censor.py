def censor(text, word):
    s = text
    i = 0
    a = ""
    for each in word:
        i += 1
    a = ("*" * i)
    b = text.replace(word, a)
    return b

sentence = raw_input("What do you want to tell the world?")
nono = raw_input("Now, let's NSA that shizzle!")

print censor(sentence, nono)