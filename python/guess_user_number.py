from random import randint
user = randint(0,999)
comp= randint(0,999)
low = 0
high = 1000
guesses = 0
while user != comp:
	comp = (low + high) / 2
	print "secret number: " + str(user)
	print "the guess is: " + str(comp)
	if comp > user:
		print "too high"
		high = comp
	if comp < user:
		print "too low"
		low = comp
	guesses += 1
else:
	print "you win"
	print "it only took %s guesses." %(guesses)