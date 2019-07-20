#!/usr/bin/python3

from AI import AI, Person
from ttt_board import Cell_Value, TTT_Board
import numpy as np

if __name__ == '__main__':
	# Get player number
	person_1 = Person(Cell_Value.PLAYER_1)
	person_2 = AI(Cell_Value.PLAYER_2)

	# init board
	board = TTT_Board()

	# Set any initial board state
	# board.update((0,0), person_1.player_symbol)
	# board.update((0,1), person_2.player_symbol)
	# board.update((0,2), person_1.player_symbol)
	# board.update((1,0), person_2.player_symbol)
	# board.update((1,1), person_1.player_symbol)
	# board.update((1,2), person_2.player_symbol)
	# board.update((2,0), person_1.player_symbol)
	# board.update((2,1), person_2.player_symbol)
	# board.update((2,2), person_1.player_symbol)

	# Play turns until win
	while( True ):
		print('PLAYER 1 TURN\n',board, sep='')
		# Does python really not have a do while?
		player_1_move = None
		while(player_1_move not in board.get_moves()):
			player_1_move =person_1.play_turn(board)
		board.update(player_1_move, person_1.player_symbol)
		print('PLAYER 2 TURN\n',board, sep='')
		player_2_move = None
		while(player_2_move not in board.get_moves()):
			player_2_move =person_2.play_turn(board)
		board.update(player_2_move, person_2.player_symbol)

