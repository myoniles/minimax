from enum import Enum
import numpy as np

# This might be a little overkill but I would rather not run into a case
# of there being a 'w' and the program getting mad
# Typed FTW
class Cell_Value(Enum):
	UNCLAIMED = ' '
	PLAYER_1 = 'X'
	PLAYER_2 = 'Y'

class TTT_Board:

	""" Represnts the entire board, really just wraps an array"""

	def __init__(self):
		self.state = [ [Cell_Value.UNCLAIMED] * 3 ] * 3

	def check_win(self):
		"""Returns the player who has won the board.
		Returns UNCLAIMED if no player has won
		:returns: Cell_Value
		"""
		players = [ _ for _ in Cell_Value if _.value != ' ']
		for player in players:
			# TODO: find a more elegant way to check diagonals
			diag = \
				np.all(np.array([self.state[0][0], self.state[1][1], self.state[2][2]]) == player) \
				or np.all( np.array([self.state[0][2], self.state[1][1], self.state[2][0]])  == player)
			if (\
				np.any((np.all(np.array(self.state) == player, axis=1))) or \
				np.any((np.all(np.array(self.state) == player, axis=0))) or \
				diag ):
				return player
		return Cell_Value.UNCLAIMED

	def get_moves(self):
		"""Gets the list of all unclaimed positions
		:returns: [(Cell_Value), ]

		"""
		return zip(*np.where(self.state == Cell_Value.UNCLAIMED))

	def __str__(self):
		"""Prints the board
		"""
		for row in self.state:
			for col in row:
				print( '|', col.value, end='' )
			print( '|' )
