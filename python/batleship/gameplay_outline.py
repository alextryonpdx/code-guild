# OPENNING SCREEN
# clears screen and shows name
# prints the rules at the begining of each game
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

def p1_menu():
	# 3 choices menu:
	print "What do you want to do?"
	print "1. View your ships"
	print "2. View your shots"
	print "3. Take a shot"
	turn_choice = raw_input("Select 1-2-3")
	if turn_choice == "1":
		p1_view_ships()
	if turn_choice == "2":
		p1_view_shots()
	if turn_choice == "3":
		p1_take_shot()
	else:
		print "Try again"
		p1_menu()

def p1_view_ships():
	# display ship_board1
	to_menu = raw_input("To return to menu press any key")
	if to_menu:
		p1_menu()

def p1_view_shots():
	# display shot_board1
	to_menu = raw_input("To return to menu press any key")
	if to_menu:
		p1_menu()

def p1_take_shot():
	# display shot_board1
	# prompt for coordinates of new shot
	# check for presence of boat in same coordinates on ship_board2
	# if hit, 
		# mark " X " on ship_board2 
		# mark " X " on shot_board1
		p1_check_sink()
		# p1_take_shot()
	# else:
		# mark " X " on ship_board2 
		# mark " X " on shot_board1 
		# print " YOU MISSED."
		# prompt press any key to clear screen and pass to player 2
		# print "\n"*15
		# prompt "ready Player 2 press any key"
		# p2_menu()

def p2_menu():
	# 3 choices menu:
	print "What do you want to do?"
	print "1. View your ships"
	print "2. View your shots"
	print "3. Take a shot"
	turn_choice = raw_input("Select 1-2-3")
	if turn_choice == "1":
		p2_view_ships()
	if turn_choice == "2":
		p2_view_shots()
	if turn_choice == "3":
		p2_take_shot()
	else:
		print "Try again"
		p2_menu()

def p2_view_ships():
	# display ship_board1
	to_menu = raw_input("To return to menu press any key")
	if to_menu:
		p2_menu()

def p2_view_shots():
	# display shot_board2
	to_menu = raw_input("To return to menu press any key")
	if to_menu:
		p2_menu()

#def p2_take_shot():
	# display shot_board1
	# prompt for coordinates of new shot
	# check for presence of boat in same coordinates on ship_board1
	# if hit, 
		# mark " X " on ship_board1 
		# mark " X " on shot_board2
		# p2_take_shot()
	# else:
		# mark " O " on ship_board1 
		# mark " O " on shot_board2 
		# print " YOU MISSED."
		# prompt press any key to clear screen and pass to player 1
		# print "\n"*15
		# prompt "ready Player 1 press any key"
		# p1_menu()

def p1_check_sink():
	if 'b' or 'c' or 'd' or 's' or 'i' in ship_board2:
		if 'b' not in ship_board2:
			print "You've sunk their BATTLESHIP"
		if 'c' not in ship_board2:
			print "You've sunk their CARRIER"
		if 'd' not in ship_board2:
			print "You've sunk their DESTROYER"
		if 's' not in ship_board2:
			print "You've sunk their SUBMARINE"
		if 'i' not in ship_board2:
			print "You've sunk their INTERCEPTOR"
		else:
			p1_take_shot()
	else:
		print "Player 1 wins"

def p2_check_sink():
	if 'b' or 'c' or 'd' or 's' or 'i' in ship_board2:
		if 'b' not in ship_board1:
			print "You've sunk their BATTLESHIP"
		if 'c' not in ship_board1:
			print "You've sunk their CARRIER"
		if 'd' not in ship_board1:
			print "You've sunk their DESTROYER"
		if 's' not in ship_board1:
			print "You've sunk their SUBMARINE"
		if 'i' not in ship_board1:
			print "You've sunk their INTERCEPTOR"
		else:
			p2_take_shot()
	else:
		print "Player 2 wins"



