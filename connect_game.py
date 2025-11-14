#Griffin Makari
#gom2018
#Assignment2

import os, time, random

#CONSTANT GLOBAL VARIABLES SECTION
Board_Columns = 7
Board_Rows = 6
col_headers = [chr(ord("A")+i) for i in range(Board_Columns)]#Column Labels that cater for a specified column board
no_of_players = 2#Assuming A standard two-player game
checkers = ["X", "O", "V", "H", "M"]#Checkers for 2 to 5 players 

#FUNCTIONS DEFINITION
def clear_screen(): #To Be Used Often Hence Function Defined
	os.system("clear")

#2D Board with all elements initialised with a white space
def create_board(rows, cols):
	return [[" " for _ in range(cols)] for _ in range(rows)]

#To Print the current state of the board 
def print_board(board):
	clear_screen()
	#print the column headers
	print("\n" + "  " + "   ".join(col_headers))
	print("+"+ "---+" * Board_Columns)

	#Rows with pieces printing(Good For Practice)
	for r in range(Board_Rows):
		#Notice the extra spaces? It makes the board visually appealing
		print("| "+" | ".join(board[r]) + " |")
		print("+" + "---+"*Board_Columns)
	print()

def is_valid_location(board, col_index):
	#Checks the row if full. Useful to determine DRAW
	return board[0][col_index] == " "


def get_next_open_row(board, col_index):
	#Moving from down up to look for the next empty space for the checkers
	for r in range(Board_Rows - 1, -1, -1):
		if board[r][col_index] == " ":
			return r
	return None #signals not empty row!

#Optional: Added for efect
def animate_drop(board, col_index, piece):
    final_row = get_next_open_row(board, col_index)

    
    for r in range(final_row + 1):#Basically Caters for the edges. Adapts to all types of boards
        board[r][col_index] = piece
        print_board(board)
        time.sleep(0.03) # The Goal of the animation function
        # Erase the piece from the current spot before it moves to the next
        if r != final_row:
            board[r][col_index] = " "

def check_win(board):
	rows = len(board)
	cols = len(board[0])
	#check horizontal
	for r in range(rows):
		for c in range(cols - 3):
			piece = board[r][c]
			if piece != " " and piece == board[r][c+1] and piece == board[r][c+2] and piece == board[r][c+3]:
				return True
	#check vertical
	for r in range(rows - 3):
		for c in range(cols):
			piece = board[r][c]
			if piece != " " and piece == board[r+1][c] and piece == board[r+2][c] and piece == board[r+3][c]:
				return True
				

	#Down Right 
	for r in range(rows-3):#Makes sure we dont go out of bounds
		for c in range(cols-3):
			piece = board[r][c]
			if piece !=" " and piece == board[r+1][c+1] and piece == board[r+2][c+2] and piece == board[r+3][c+3]:
				return True

	#Down Left Checker
	for r in range(rows-3):#Makes sure we dont go out of bounds
		for c in range(3, cols):
			piece = board[r][c]
			if piece !=" " and piece == board[r+1][c-1] and piece == board[r+2][c-2] and piece == board[r+3][c-3]:
				return True
	return False #If no win is found!!

def is_board_full(board):
	COLS = Board_Columns
	state = all(board[0][c] != " " for c in range(COLS))
	return state
def main():
	
	game_over = False
	turn = random.randint(0, no_of_players-1)#Random turn determined 
	playing_board = create_board(Board_Rows, Board_Columns)
	print_board(playing_board)
	while not game_over:
		#Determining CUrrent Players Piece
		current_checker = checkers[turn % len(checkers)]
		player_number = turn + 1

		#First Part of the Game. 
		while True:
			#Class Material
			try:
				choice = input(f"Player {turn+1}, please enter a column:  ")
			except:
				print("INVALID CHARACTER")

		
			#Input Validation
			if choice not in col_headers:
				print(f"Invalid Column {choice}. Please enter a letter from {col_headers[0]} to {col_headers[-1]}.: ")#To adapt a board of anysize
				time.sleep(1)
				print_board(playing_board)
				continue
			#To Determine to the column for the piece falls	
			col_index = col_headers.index(choice)
			if not is_valid_location(playing_board, col_index):
				print(f"TURN INVALID. You Have Entered A Checker To A Full Column")
				time.sleep(1)
				#Player Loses Turn
				print_board(playing_board)
				turn = (turn+1)%no_of_players
				continue

			break

		#Second Part (Moving The Piece) - This is optional added for practice
		row_index = get_next_open_row(playing_board, col_index) #Get the row to place the checker piece!!

		animate_drop(playing_board, col_index, current_checker)
		#3rd Part of the game checking for the win!!
		if check_win(playing_board):
			print_board(playing_board) # Final Board
			print(f"\nCONGRATULATIONS Player {player_number} of [{current_checker}] WINS!!!!\n")
			game_over = True
		elif is_board_full(playing_board):
			print_board(playing_board) # FINAL BOARD
			print("\n GAME OVER IT IS A DRAW!!\n")
			game_over = True
		if not game_over:
			turn = (turn + 1)% no_of_players# Players Taking Turn Placing Checkers
	print('Thanks for playing!!')

#For Readablity in this case I will employ this
if __name__ == '__main__':
	main()