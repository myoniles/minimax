from AI import AI, Person
from ttt_board import Cell_Value, TTT_Board

if __name__ == '__main__':
	# Get player number
	person_1 = Person(Cell_Value.PLAYER_1)
	person_2 = AI(Cell_Value.PLAYER_2)

	# init board
	board = TTT_Board()

	# Play turns until win
	while( True ):
		print(board)
		person_1.play_turn(board)
		print(board)
		person_2.play_turn(board)

