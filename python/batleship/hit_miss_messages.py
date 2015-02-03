def miss_message():
	from random import randint
	miss_scripts = [
		"Captain... I think we hit a fish",
		"Maybe the torpedo was caught in a cross-current.",
		"You'll get 'em next time.",
		"KER-PLUNK.",
		"Poseidon is not on your side.",

	]
	script = randint(0, len(miss_scripts) - 1)
	print miss_scripts[script]

def hit_message():
	from random import randint
	hit_scripts = [
		"BOOM!",
		"You got 'em",
		"That one did some real damage",
		"What a shot!",
		"You smoked 'em, Captain.",
		"Welcome to erf."
	]
	script = randint(0, len(hit_scripts) - 1)
	print hit_scripts[script]

def open_screen():
	print "\n"*10
	print "WELCOME TO BATTLESHIP"
	print "********RULES********"
	print "Each player will place 5 ships"
	print "After placing ships the game begins"
	print "At the start of your turn you have three choices:"
	print "    1. You can look at your ships"
	print "    2. You can look at the shots you have taken"
	print "    3. You can take a shot at your opponent"
	print "If you miss, an 'O' will appear and your opponent will have a turn"
	print "If you hit a ship and 'X' will appear and you will shoot again"
	print "First person to destroy the enemy's fleet wins"
	start_game = raw_input("To start game press any key")
	player_select()
	# run ship placement function for p1
	# clear screen
	# run ship placement function for p2
	# clear screen
	# p1_menu()

def player_select():
	print "Are you Captain 1 or Captain 2?"
	player = raw_input("Enter 1 or 2: ")
	if player == "1":
		player = "player1"
	elif player == "2":
		player = "player2"
	else:
		player_select()