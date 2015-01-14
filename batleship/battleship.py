import os

def clear_screen():
	os.system("clear")

# OPENNING SCREEN
# clears screen and shows name
# prints the rules at the begining of each game


def open_screen():
	clear_screen()
	print "WELCOME TO BATTLESHIP"
	print "********RULES********"
	print ""
	print "Each player will place 5 ships"
	print "After placing ships the game begins"
	print "At the start of your turn you have three choices:"
	print "    1. You can view your fleet position"
	print "    2. You can view the shots you have taken"
	print "    3. You can fire at your opponent's fleet"
	print "If you miss, an 'O' will appear and your opponent will have a turn"
	print "If you hit a ship an 'X' will appear and you will shoot again"
	print "First Captain to destroy the enemy's fleet wins!"
	print ""
	start_game = raw_input("To start game press any key")
	clear_screen()
	# run ship placement function for p1
	# clear screen
	# run ship placement function for p2
	# clear screen
	# p1_menu()

def player1_menu():
# 3 choices menu:
	clear_screen()
	print "*** Player 1 Command Center ***"
	print "What do you want to do?"
	print "1. View your fleet"
	print "2. View your shots"
	print "3. Fire at opponent"
	turn_choice = raw_input("Select 1-2-3: ")

	if turn_choice == "1":
		view_fleet("player1")
	if turn_choice == "2":
		view_shots("player1")
	if turn_choice == "3":
		fire_shot("player1")
	else:
		print "That's not a valid selection, try again"
		player1_menu()

def player2_menu():
# 3 choices menu:
	clear_screen()
	print "*** Player 2 Command Center ***"
	print "What do you want to do?"
	print "1. View your fleet"
	print "2. View your shots"
	print "3. Fire at opponent"
	turn_choice = raw_input("Select 1-2-3: ")

	if turn_choice == "1":
		view_fleet("player2")
	if turn_choice == "2":
		view_shots("player2")
	if turn_choice == "3":
		fire_shot("player2")
	else:
		print "That's not a valid selection, try again"
		player2_menu()


def view_fleet(player):
	if player == "player1":
		print_board(player1, "SHIP_BOARD")
		to_menu = raw_input("To return to menu press any key")
		if to_menu:
			player2_menu()
	elif player == "player2":
		print_board(player2, "SHIP_BOARD")
		to_menu = raw_input("To return to menu press any key")
		if to_menu:
			player2_menu()
	else:
		print "error"


def view_shots(player):
	# display shot_board1
	if player == "player1":
		print_board(player1, "SHOT_BOARD")
		to_menu = raw_input("To return to menu press any key")
		if to_menu:
			player1_menu()
	elif player == "player2":
		print_board(player2, "SHOT_BOARD")
		to_menu = raw_input("To return to menu press any key")
		if to_menu:
			player2_menu()
	else:
		print "error"







def fire_shot(player):
	if player == "player1":
		print "What coordinates are we firing at Captain?"
		fire_row = row_ask()
		fire_column = column_ask()
		# could cut down with hit and miss functions
		if player2["SHIP_BOARD"][fire_row][fire_column] in "BCDSI":
			player1["SHOT_BOARD"][fire_row][fire_column] = " X "
			clear_screen()
			print "You smoked em' Captain"
			player1_menu()
		else:
			player1["SHOT_BOARD"][fire_row][fire_column] = " O "
			clear_screen()
			print "Captain... I think we hit a fish"
			turn_change = raw_input("Player 2, are you ready?")
			player2_menu()
	elif player == "player2":
		print "What coordinates are we firing at Captain?"
		fire_row = row_ask()
		fire_column = column_ask()
		if player1["SHIP_BOARD"][fire_row][fire_column] in "BCDSI":
			player2["SHOT_BOARD"][fire_row][fire_column] = " X "
			clear_screen()
			print "You smoked em' Captain"
			player2_menu()
		else:
			player2["SHOT_BOARD"][fire_row][fire_column] = " O "
			clear_screen()
			print "Captain... I think we hit a fish"
			turn_change2 = raw_input("Player 1, are you ready?")
			player1_menu()



def create_board():
	board = []
	for row in range(10):
		board.append([])
		for column in range(10):
			board[row].append(" - ")
	return board

player1 = {"SHIP_BOARD": None, "SHOT_BOARD": None}

player2 = {"SHIP_BOARD": None, "SHOT_BOARD": None}

def print_board(player, board_type):
	for x in range(10):
		print player[board_type][x]


def row_ask():
	row_map = {"A": 0, "B": 1, "C": 2,
				"D": 3, "E": 4, "F": 5,
				"G": 6, "H": 7, "I": 8,
				"J": 9}
	row = raw_input("Row A-J: ").upper()
	
	if row not in "ABCDEFGHIJ" or row == "":
		print("please try again")
		return row_ask()
	else:
		return row_map[row]
	
def column_ask():
	column_map = {1: 0, 2: 1, 3: 2,
					4: 3, 5: 4, 6: 5,
					7: 6, 8: 7, 9: 8,
					10: 9}
	column = int(raw_input("Column 1-10: "))

	if column not in range(1, 11):
		print("please try again")
		return column_ask()
	else:
		return column_map[column]

# def draw_ship(num):
	# draw ship onto the board
	# called by assign_ship	

def assign_ship():
	# to-do: pass in a ship argument
	print "Assign your coordinates Captain"
	row = row_ask()
	column = column_ask()
	# bow = board[int(raw_input("0-9: "))][int(raw_input("0-9: "))] = "ship"
	# to-do: handle ship orientation N, S, E, or W	
	orientation_ask()
	# board[row][column] = "ship"
	# return draw_ship(int value)"""

def place_ships(player):
	ships = {"Destroyer": 4}
		#"Carrier": 5,
		#"Battleship": 3, 
		#"Submarine": 3, 
		#"Interceptor": 2}


	def assign_ship():
		print "Assign your coordinates Captain"
		row = row_ask()
		column = column_ask()
		bow = [row, column]
		# bow = board[int(raw_input("0-9: "))][int(raw_input("0-9: "))] = "ship"
		# to-do: handle ship orientation N, S, E, or W	
		return orientation_ask(bow)

	def orientation_ask(bow):
		"""
		@bow list -> the starting point of the ship
		"""
		orientation = raw_input("Which direction will your ship go?" + "\n"
			+ "(N)orth, (S)outh, (E)ast, or (W)est? ").upper()
		ship_length = ships[ship]
		if orientation not in "NSEW":
			orientation_ask(bow)

		else:
#			check_ship(bow, ship_length, orientation)
			draw_ship(bow, ship_length, orientation)

	def draw_ship(bow, ship_length, orientation):
		"""
		@bow list -> the starting point of the ship
						e.g. (row, column)
						these values are used to lookup positions
						in the main ship board
		@ship_length int -> the length of the ship from the ships dictionary
		@orientation str -> the direction the boat is heading
		"""

		if player["SHIP_BOARD"][bow[0]][bow[1]] != " - ":
			print_board(player, SHIP_BOARD)
			print "Your ships cannot overlap"
			print "%s, %s spaces." %(ship, ships[ship])
			assign_ship()


# NEED A CHECK FOR SHIPS RUNNING OFF BOARD
# OR A NEW RULE THAT ALLOWS SHIPS TO BRIDGE THE INFINITY
		else:
			player["SHIP_BOARD"][bow[0]][bow[1]] = " " + ship[0] + " "
			while ship_length != 0:
				# establish bow position
				# draw incremented ship position
				player["SHIP_BOARD"][bow[0]][bow[1]] = " " + ship[0] + " "
				# check orientation
				# increment board position
				if orientation == "E":
					bow[1] -= 1
				elif orientation == "W":
					bow[1] += 1
				elif orientation == "N":
					bow[0] += 1
				elif orientation == "S":
					bow[0] -= 1
				# decrement ship length after marking position
				ship_length -= 1
			print_board(player, "SHIP_BOARD")

	
	for ship in ships:
		print ""
		print("Mobilizing Fleet")
		print ""
		print_board(player, "SHIP_BOARD")
		print ""
		print "%s, %s spaces." %(ship, ships[ship])
#	board[row][column] = "ship"
#	return draw_ship(int value)
		assign_ship()			

open_screen()
player1["SHIP_BOARD"] = create_board()
player1["SHOT_BOARD"] = create_board()
player2["SHIP_BOARD"] = create_board()
player2["SHOT_BOARD"] = create_board()
print "PLAYER 1"
place_ships(player1)
switch_player = raw_input("Press any key to clear screen for Player 2's to place their ships")
clear_screen()
print "PLAYER 2"
place_ships(player2)
switch_player2 = raw_input("Press any key to clear screen for Player 1's turn")
clear_screen()
player1_menu()

""" def prompt_fire(player):
	print "What coordinates are we firing at Captain?"
	fire_row = row_ask()
	fire_column = column_ask()

	if player[fire_row][fire_column] in "bcdsi" or "BCDSI":
		SHOT_BOARD[fire_row][fire_column] = "hit"
		print "You smoked em' Captain"
		player1_menu()
	else:
		SHOT_BOARDB[fire_row][fire_column] = "miss"
		print "Captain... I think we hit a fish"
		player2_menu() """

# print_board()
