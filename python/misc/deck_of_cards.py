from random import randint
game = '0'
while str(game) != '9':
	hand1 = []
	hand2 = []
	flip = []
	flop = []
	river = []
	again = 0
	deck = {
	1:['x','cA','c2','c3','c4','c5','c6','c7','c8','c9','c10','cJ','cQ','cK'],
	2:['x','sA','s2','s3','s4','s5','s6','s7','s8','s9','s10','sJ','sQ','sK'],
	3:['x','dA','d2','d3','d4','d5','d6','d7','d8','d9','d10','dJ','dQ','dK'],
	4:['x','hA','h2','h3','h4','h5','h6','h7','h8','h9','h10','hJ','hQ','hK']
	}

	def deal(how_many):
		x = 0
		while how_many > x:
			suit = randint(1,4)
			card = randint(1,13)
			while deck[suit][card] == 'x':
				suit = randint(1,4)
				card = randint(1,13)
			print deck[suit][card]
			hand1.append(deck[suit][card])
			deck[suit][card] = 'x'
			x += 1
		else:
			return

			
	print "Let's Play Cards"
	print "1. Five Card Stud"
	print "2. Seven Card Stud"
	print "3. Texas Hold'em"
	print "4. Deal a hand"
	print "9. Quit"

	


	game = raw_input("What do you want to play?")

	if str(game) == '1':
		#deal five card stud:

		a = 0
		print "\n player one"
		while a != 12: 
			if a < 5:
				suit = randint(1,4)
				card = randint(1,13)
				while deck[suit][card] == 'x':
					suit = randint(1,4)
					card = randint(1,13)
				# print deck[suit][card]
				hand1.append(deck[suit][card])
				deck[suit][card] = 'x'
				a += 1
			if a == 5:
				print hand1
				print "\n player two"
				a += 1
			if a < 12 and a > 5:
				suit = randint(1,4)
				card = randint(1,13)
				while deck[suit][card] == 'x':
					suit = randint(1,4)
					card = randint(1,13)
				# print deck[suit][card]
				hand2.append(deck[suit][card])
				deck[suit][card] = 'x'
				a += 1
			if a == 11:
				print hand2
				print '\n'
		end_game = raw_input("Return to menu? y, n: ")
		if end_game.lower == 'y':
			a += 1
		
		else:
			game = '0'
		
	if str(game) == '2':
		#deal seven card stud:
		from random import randint

		a = 0
		print "player one"
		while a != 16: 
			if a < 7:
				suit = randint(1,4)
				card = randint(1,13)
				while deck[suit][card] == 'x':
					suit = randint(1,4)
					card = randint(1,13)
				# print deck[suit][card]
				hand1.append(deck[suit][card])
				deck[suit][card] = 'x'
				a += 1
			if a == 7:
				print hand1
				print "\n player two"
				a += 1
			if a < 15 and a > 7:
				suit = randint(1,4)
				card = randint(1,13)
				while deck[suit][card] == 'x':
					suit = randint(1,4)
					card = randint(1,13)
				# print deck[suit][card]
				hand2.append(deck[suit][card])
				deck[suit][card] = 'x'
				a += 1
			if a == 15:
				print hand2
				print "\n"
				a += 1
		end_game = raw_input("Return to menu? y, n: ")
		if end_game.lower == 'y':
			a += 1
		else:
			game = '0'

	if str(game) == '3':
		#Deal Texas Hold'em
		from random import randint
		a = 0
		print "player one"
		while a != 23: 
			if a < 6:
				suit = randint(1,4)
				card = randint(1,13)
				while deck[suit][card] == 'x':
					suit = randint(1,4)
					card = randint(1,13)
				# print deck[suit][card]
				hand1.append(deck[suit][card])
				deck[suit][card] = 'x'
				a += 1
			if a == 6:
				print hand1
				print "\n player two"
				a += 1
			if a < 12 and a > 6:
				suit = randint(1,4)
				card = randint(1,13)
				while deck[suit][card] == 'x':
					suit = randint(1,4)
					card = randint(1,13)
				# print deck[suit][card]
				hand2.append(deck[suit][card])
				deck[suit][card] = 'x'
				a += 1
			if a == 12:
				print hand2
				print "\n the flop"
				a += 1
			if a == 13:
				suit = randint(1,4)
				card = randint(1,13)
				while deck[suit][card] == 'x':
					suit = randint(1,4)
					card = randint(1,13)
				deck[suit][card] = 'x'
				a += 1
			if a < 16 and a > 13:
				suit = randint(1,4)
				card = randint(1,13)
				while deck[suit][card] == 'x':
					suit = randint(1,4)
					card = randint(1,13)
				# print deck[suit][card]
				flop.append(deck[suit][card])
				deck[suit][card] = 'x'
				a += 1
			if a == 16:
				print flop
				print "\n the flip"
				a += 1
			if a == 17:
				suit = randint(1,4)
				card = randint(1,13)
				while deck[suit][card] == 'x':
					suit = randint(1,4)
					card = randint(1,13)
				deck[suit][card] = 'x'
				a += 1
			if a == 18:
				suit = randint(1,4)
				card = randint(1,13)
				while deck[suit][card] == 'x':
					suit = randint(1,4)
					card = randint(1,13)
				# print deck[suit][card]
				flip.append(deck[suit][card])
				deck[suit][card] = 'x'
				a += 1
			if a == 19:
				print flip
				print "\n the river"
				a += 1
			if a == 20:
				suit = randint(1,4)
				card = randint(1,13)
				while deck[suit][card] == 'x':
					suit = randint(1,4)
					card = randint(1,13)
				deck[suit][card] = 'x'
				a += 1
			if a == 21:
				suit = randint(1,4)
				card = randint(1,13)
				while deck[suit][card] == 'x':
					suit = randint(1,4)
					card = randint(1,13)
				# print deck[suit][card]
				river.append(deck[suit][card])
				deck[suit][card] = 'x'
				a += 1
			if a == 22:
				print river
				a += 1
		end_game = raw_input("Return to menu? y, n: ")
		if end_game.lower == 'y':
			a += 1
		else:
			game = '0'

	
	if str(game) == "4":
		while again  != "n":
			how_many = int(raw_input("How many cards would you like?"))
			print "hand 1: %s" %(deal(how_many))
			print "\n"
			print "hand 2: %s" %(deal(how_many))
			again = raw_input("Play again? (y, n): ")
		



	if str(game) == 9:
		quit()