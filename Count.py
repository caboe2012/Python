#Needs work.  Current funtion only grabs one element at a time.  need to add functionality for n-grams.

instances = 0
def count(sequence, item):
    instances = 0
    for each in sequence:
    	if item == each:
        	instances += 1
    	print instances
    return instances

user1 = raw_input("Enter a list:")
user2 = raw_input("Enter an item to tally:")


count(user1, user2)

print ("There are {instances} occurrences of the following word: {user2}.".format(**vars()))

