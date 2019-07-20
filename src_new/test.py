from ttt_board import TTT_Board, Cell_Value

def test_function( test_function ):
	status_str = 'Passed'
	try:
		test_function()
	except AssertionError:
		status_str = 'Failed - Assertion Error'
	except:
		status_str = 'Failed - Internal Error'
	print( test_function.__name__, ':', status_str)

#-----------------
#-  Enum Tests?  -
#-----------------

#-----------------
#-  Board Tests  -
#-----------------

def check_win_unassigned():
	board = TTT_Board()
	assert( board.check_win() == Cell_Value.UNCLAIMED)

if __name__ == '__main__':
	test_function(check_win_unassigned)
