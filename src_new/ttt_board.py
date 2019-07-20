from enum import Enum
import numpy as np

# This might be a little overkill but I would rather not run into a case
# of there being a 'w' and the program getting mad
# Typed FTW
class Cell_Value(Enum):
	UNCLAIMED = ' '
	PLAYER_1 = 'X'
	PLAYER_2 = 'O'

class TTT_Board:

	""" Represnts the entire board, really just wraps an array"""

	def __init__(self, initial_state=None):
		if not initial_state:
			self.state = np.array([ [Cell_Value.UNCLAIMED] * 3 ] * 3)
		else:
			self.state = initial_state.state.copy()

	def check_win(self):
		"""Returns the player who has won the board.
		Returns UNCLAIMED if no player has won
		:returns: Cell_Value
		"""
		players = [ _ for _ in Cell_Value if _.value != ' ']
		for player in players:
			# TODO: find a more elegant way to check diagonals
			diag = np.all(np.array([self.state[0][0], self.state[1][1], self.state[2][2]]) == player) or np.all( np.array([self.state[0][2], self.state[1][1], self.state[2][0]])  == player)
			horiz = np.any((np.all(self.state == player, axis=0)))
			vert = np.any((np.all(self.state == player, axis=1)))
			if ( horiz or vert or diag ):
				return player
		return Cell_Value.UNCLAIMED

	def get_moves(self):
		"""Gets the list of all unclaimed positions
		:returns: [(Cell_Value), ]

		"""
		return tuple(zip(*np.where(self.state == Cell_Value.UNCLAIMED)))

	def __str__(self):
		"""Prints the board"""
		_ = ""
		for row in self.state:
			for col in row:
				_  = _ + '|' + str(col.value)
			_ = _ + '|\n'
		return _

	def to_num_arr(self):
		"""TODO: Docstring for to_num_arr.
		:returns: TODO

		"""
		translation_dict = { Cell_Value.PLAYER_1.value:-1,Cell_Value.PLAYER_2.value:1, Cell_Value.UNCLAIMED.value:0 }
		vectorized_board = np.vectorize(lambda enum: translation_dict[enum.value])
		return vectorized_board(self.state)

	def update(self, move, player_value):
		if move[0] == -1 :
			return
		self.state[move] = player_value

