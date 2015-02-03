board = []
# letters = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J")



for row in range(10):
	board.append([])
	for column in range(10):
		board[row].append(" - ")

def validate_row_input(user_input):
	print "the input before checking is %s" % user_input
	if user_input:
		if user_input not in "ABCDEFGHIJ":
			print("please choose one letter A-J")
			row_ask()
		else:
			# print "the input after the check is %s" % user_input
			return user_input
	else:
		print("don't be a dick")
		row_ask()

def validate_column_input(user_input):
	if user_input not in range(1, 11):
		print("column must be between 1 and 10")
		column_ask()
	else:
		return user_input

def row_ask():
	row_map = {"A": 0, "B": 1, "C": 2,
				"D": 3, "E": 4, "F": 5,
				"G": 6, "H": 7, "I": 8,
				"J": 9}
	row = raw_input("Row A-J: ")
	# print "row before validator is %s" % row
	# print "the number from row_map is %d" % row_map[row]
	validate_row_input(row)
	return row_map[row]
	
def column_ask():
	column_map = {1: 0, 2: 1, 3: 2,
					4: 3, 5: 4, 6: 5,
					7: 6, 8: 7, 9: 8,
					10: 9}
	column = int(raw_input("Column 1-10: "))
	validate_column_input(column)
	return column_map[column]


# def draw_ship(num):
	# draw ship onto the board
	# called by assign_ship	

"""def assign_ship():
	# to-do: pass in a ship argument
	print "Assign your coordinates Captain"
	row = row_ask()
	column = column_ask()
	# bow = board[int(raw_input("0-9: "))][int(raw_input("0-9: "))] = "ship"
	# to-do: handle ship orientation N, S, E, or W	
	orientation_ask()
	# board[row][column] = "ship"
	# return draw_ship(int value)"""

def place_ships():
	ships = {"destroyer": 4,
		"carrier": 5,
		"battleship": 3, 
		"submarine": 3, 
		"interceptor": 2}


	def orientation_ask(bow):
		"""
		@bow list -> the starting point of the ship
		"""
		orientation = raw_input("Which direction will your ship go?" + "\n"
			+ "(N)orth, (S)outh, (E)ast, or (W)est? ")
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

		if board[bow[0]][bow[1]] != " - ":
			print_board()
			print "Your ships cannot overlap"
			print "%s, %s spaces." %(ship, ships[ship])
			assign_ship()
# NEED A CHECK FOR SHIPS RUNNING OFF BOARD
# OR A NEW RULE THAT ALLOWS SHIPS TO BRIDGE THE INFINITY
		else: 
			board[bow[0]][bow[1]] = " " + ship[0] + " "
			while ship_length != 0:
				# establish bow position
				# draw incremented ship position
				board[bow[0]][bow[1]] = " " + ship[0] + " "
				# check orientation
				# increment board position
				if orientation == "E":
					bow[1] += 1
				elif orientation == "W":
					bow[1] -= 1
				elif orientation == "N":
					bow[0] -= 1
				elif orientation == "S":
					bow[0] += 1
				# decrement ship length after marking position
				ship_length -= 1
			
	


	def assign_ship():
		# to-do: pass in a ship argument
		print "Assign your coordinates Captain"
		row = row_ask()
		column = column_ask()
		bow = [row, column]
		# bow = board[int(raw_input("0-9: "))][int(raw_input("0-9: "))] = "ship"
		# to-do: handle ship orientation N, S, E, or W	
		return orientation_ask(bow)
	
	for ship in ships:
		print("get ready to place your ship")
		print_board()
		print "%s, %s spaces." %(ship, ships[ship])
#	board[row][column] = "ship"
#	return draw_ship(int value)
		assign_ship()			
def print_board():
	for x in range(10):
		print board[x]

place_ships()
print_board()

# print_board()
