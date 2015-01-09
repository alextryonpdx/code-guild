from random import randint
user = randint(2,999)
comp= randint(2,999)
low = 0
high = 1000
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
else:
	print "you win"