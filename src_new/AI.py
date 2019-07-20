from ttt_board import Cell_Value, TTT_Board
import numpy as np

class Person:

	"""Docstring for Person. """

	def __init__(self, player_symbol):
		"""TODO: to be defined1. """
		self.player_symbol= player_symbol

	def play_turn(self, board):
		"""TODO: Docstring for play_turn.

		:board: TODO
		:returns: TODO

		"""
		x_cord = input("X cord: ")
		y_cord = input("Y cord: ")
		return (int(x_cord), int(y_cord))

class AI(Person):

	"""Docstring for AI. """

	MAX_EVAL = 100
	MIN_EVAL = -100

	def __init__(self, player_symbol):
		"""TODO: to be defined1. """
		super(AI, self).__init__( player_symbol )

	def eval(self, board):
		"""TODO: Docstring for eval.

		:board: TODO
		:returns: TODO

		"""
		mask = np.array([[3, 2, 3], [2, 3, 2],[3, 2, 3]])
		return np.sum( board.to_num_arr() * mask )

	def play_turn(self, board):
		"""TODO: Docstring for play_turn.

		:board: TODO
		:returns: ( x cord, y cord )

		"""
		rate, move = self.minimax(board, True)
		return move

	def minimax(self, board, max_player=True, max_depth=3 ):
		"""TODO: Docstring for minimax.

		:board: TODO
		:returns: TODO

		"""
		moves = board.get_moves()
		if max_depth == None:
			max_depth = len(moves)

		# Game is over if no moves (cat's game) or already won
		if max_depth < 0 or moves == [] or board.check_win() != Cell_Value.UNCLAIMED:
			if board.check_win() == self.player_symbol:
				return AI.MAX_EVAL * (9-max_depth), (-1,-1)
			elif board.check_win() == Cell_Value.UNCLAIMED:
				return self.eval(board) * (9-max_depth), (-1,-1)
			else:
				return AI.MIN_EVAL * (9-max_depth), (-1,-1)

		possible_moves = board.get_moves()
		best_move = None
		if max_player:
			curr_eval = AI.MIN_EVAL
			for move in possible_moves:
				test_board = TTT_Board(board)
				test_board.state[move] = Cell_Value.PLAYER_2
				move_eval, enemy_move = self.minimax( test_board, False, max_depth-1)
				curr_eval = max( curr_eval, move_eval)
				if curr_eval == move_eval:
					best_move = move
		else: # Minimizing player
			curr_eval = AI.MAX_EVAL
			for move in possible_moves:
				test_board = TTT_Board(board)
				test_board.state[move] = Cell_Value.PLAYER_1
				move_eval , enemy_move = self.minimax( test_board, True, max_depth-1)
				curr_eval = min( curr_eval, move_eval)
				if curr_eval == move_eval:
					best_move = move

		return curr_eval, best_move

