class Person:

	"""Docstring for Person. """

	def __init__(self, player_symbol):
		"""TODO: to be defined1. """
		self.player_sybmbol= player_symbol

	def play_turn(self, board):
		"""TODO: Docstring for play_turn.

		:board: TODO
		:returns: TODO

		"""
		pass

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
		pass

	def minimax(self, board, max_player=True, max_depth=None ):
		"""TODO: Docstring for minimax.

		:board: TODO
		:returns: TODO

		"""
		# Game is over if no moves (cat's game) or already won
		moves = board.get_moves()
		if not max_depth or moves == [] or board.check_win != Cell_Value.UNCLAIMED:
			return board.check_win

		possible_moves = board.get_moves()
		if max_player:
			curr_eval = AI.MIN_EVAL
			for move in possible_moves:
				move_eval = minimax( board, False)
				curr_eval = max( curr_eval, move_eval)
		else: # Minimizing player
			curr_eval = AI.MAX_EVAL
			for move in possible_moves:
				move_eval = minimax( board, True)
				curr_eval = min( curr_eval, move_eval)
		return curr_eval

