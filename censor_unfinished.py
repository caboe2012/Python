    
    
    
    
    
    
    word = user.lower()
    first = word[0]  # use the variable 'first' to grab first letter of user input string 
    if first in "aeiou": # determine if 'first' is a vowel
        new_word = word + pyg # if it is a vowerl, convert it straight away
        print new_word # print the newly converted word
    else: # if 'first' is not a vowel
        word_length = len(word) # determine the length of the users word
        new_word = word[1:(word_length + 1)] + first + pyg # convert the word by slicing from the 1st offset to the last offset inclusive!!! and add on the first letter and the pig latinifier
        print new_word # print the pig latin equivalent!
else:
    print 'empty' # return this if the user input was not a single word


CENSOR
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
