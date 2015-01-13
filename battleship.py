"""
board = [
['-', '-', '-', '-', '-', '-', '-', '-', '-','-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-','-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-','-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-','-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-','-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-','-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-','-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-','-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-','-'],
['-', '-', '-', '-', '-', '-', '-', '-', '-','-']
]

print board
"""
board = []
for x in range(10):
	for y in range(10):
		board.append(' ')


"""
player will place boat, take up three spots. board[0-9][0-9] 
	for each ship one of the index variable must stay constant 
		example: (b[0]][9]-b[0][7]) (B[7][8]-b[5][8])
		each ship will be a sub-list in the 
			dictionary "ships" which will be indexed by ship name
user guess will replace indexed position with an 'X'.
will need to move that value to a new list to keep track of guesses made.
top of the chain will need to be ship placement list to check for hits.
computer will need randint generator for guesses.
	ideally will have a secondary protocol once it has made a hit and until it has sunk the ship
		hunter mode- persue hits along same-indexed lines
DISPLAY, this should be simople once we figure it out.

 """