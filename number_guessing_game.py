from random import randint
comp = randint(2,99)
user = int(0)
while user != comp:
	user = int(raw_input("Guess a number form 1 to 100:   "))
	if user > comp:
		print "too high"
	if user < comp:
		print "too low"
else:
	print "you win \n"*100