from ttt_board import Cell_Value, TTT_Board

class Person:

	"""Docstring for Person. """

	def __init__(self, player_symbol):
		"""TODO: to be defined1. """
		self.player_symbol= player_symbol

	def update(self, board, move):
		print(move)
		board.state[move] = self.player_symbol

	def play_turn(self, board):
		"""TODO: Docstring for play_turn.

		:board: TODO
		:returns: TODO

		"""
		x_cord = input("X cord: ")
		y_cord = input("Y cord: ")
		self.update(board, (int(x_cord), int(y_cord)))
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
		rate, move = self.minimax(board, True)
		print(rate)
		self.update( board, move)

	def minimax(self, board, max_player=True, max_depth=None ):
		"""TODO: Docstring for minimax.

		:board: TODO
		:returns: TODO

		"""
		# Game is over if no moves (cat's game) or already won
		moves = board.get_moves()
		if max_depth or moves == [] or board.check_win() != Cell_Value.UNCLAIMED:
			print('caught', board.check_win())
			if board.check_win() == self.player_symbol:
				return AI.MAX_EVAL, (-1,-1)
			else:
				return AI.MIN_EVAL, (-1,-1)


		possible_moves = board.get_moves()
		best_move = None
		if max_player:
			curr_eval = AI.MIN_EVAL
			for move in possible_moves:
				test_board = TTT_Board(board)
				test_board.state[move] = Cell_Value.PLAYER_2
				print(test_board)
				input()
				move_eval, enemy_move = self.minimax( test_board, False)
				curr_eval = max( curr_eval, move_eval)
				if curr_eval == move_eval:
					best_move = move
		else: # Minimizing player
			curr_eval = AI.MAX_EVAL
			for move in possible_moves:
				test_board = TTT_Board(board)
				test_board.state[move] = Cell_Value.PLAYER_1
				print(test_board)
				input()
				move_eval , enemy_move = self.minimax( test_board, True)
				curr_eval = min( curr_eval, move_eval)
				if curr_eval == move_eval:
					best_move = move

		return curr_eval, best_move

