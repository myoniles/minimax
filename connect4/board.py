import numpy as np
import math

def minimax(b, maxing=False, depth=1, max_depth=5):
	# At a definite leaf
	pm = b.possible_moves()
	b.eval()
	if b.won:
		return b.eval()/depth
	if len(pm) ==0 :
		return b.eval()
	if  depth == max_depth:
		return b.eval()

	player = "yellow"
	mod = 1
	if not maxing:
		player = "red"
		mod = -1

	node_value = mod*-1*math.inf
	m_index = 3
	for i in pm:
		# foreach, make a move, see if we are doing alright then continue
		c = b.copy()
		c.update(player,i)
		p = node_value
		if maxing:
			node_value = max(node_value, minimax(c, maxing=(not maxing), depth=depth+1, max_depth=max_depth))
		else:
			node_value = min(node_value, minimax(c, maxing=(not maxing), depth=depth+1, max_depth=max_depth))
		if p != node_value:
			m_index = i

	if depth==1:
		return (node_value,m_index)
	else:
		return node_value

class Board:
	def __init__(self,bot_step=None):
		self.state = np.zeros((6,7))
		self.bot_step = bot_step
		self.won=False

	def __str__(self):
		r_str = "|\033[1;31mR\033[0m"
		y_str = "\033[1;33mY\033[0m"
		if(self.won):
			score = self.eval()
			print("won")
			if self.eval() >= 0:
				y_str="\033[30;43mY\033[0m"
			else:
				r_str = "|\033[30;41mR\033[0m"

		s = " " + str(self.state)[1:]
		s=s.replace("[","")
		s=s.replace("]","")
		s=s.replace(" ","|")
		s=s.replace("0."," ")
		s=s.replace("\n","||\n")
		s=s.replace("-1.", r_str)
		s=s.replace("1.", y_str)
		return s + "||\n  0  1  2  3  4  5  6\n\n"

	def find_streak(self, arr, mod, k):
		#only care about the begining
		score = 0
		if arr.size < 4:
			return 0
		comp = np.logical_or(arr==0, arr == mod)
		count = arr.copy()
		count[ count != mod] = 0
		count = count ** 2

		for i in range(arr.size-3):
			# shift over until we have an opening of 4
			if (comp[i:i+4].all()):
				# Make sure there are enough to score the points
				if(np.sum(count[i:i+4]) == k ): # Strictly equal or we overcount
					score = score + k
					if ( k == 4 ):
						score = score + 1000
						self.won=True
		return mod*score


	def eval(self):
		# look at the tops of the board, where progress can be made
		# Score is the sum of a given run where the end is exposed

		# Get top
		s = (np.zeros(6)+1).dot(self.state**2) # number of items in each row
		ceil = int(np.max(s))+1
		score = 0

		for k in [2,3,4]:
			for col in range(s.size):
				score += self.find_streak(self.state[:,col], 1, k)
				score += self.find_streak(self.state[:,col],-1, k)
			for i in range(ceil):
				score += self.find_streak(self.state[5-i], 1, k)
				score += self.find_streak(self.state[5-i], -1, k)

			for diag in range(-2,4):
				score += self.find_streak(np.fliplr(self.state).diagonal(diag), 1,k)
				score += self.find_streak(np.fliplr(self.state).diagonal(diag),-1,k)
				score += self.find_streak(self.state.diagonal(diag), 1,k)
				score += self.find_streak(self.state.diagonal(diag),-1,k)

		return score



	def update(self, player, col):
		mod = 1
		if player.lower() == "red":
			mod = -1
		height=5- int(sum(self.state[:,col]**2))
		self.state[:,col][height] = mod

	def possible_moves(self, board=None):
		if(board == None):
			board = self.state
		r = np.array(range(7))
		c = board**2
		s = (np.zeros(6)+1).dot(c) # number of items in each row
		r = np.delete(r, np.where( s >= 6))
		return r

	def get_state(self):
		return self.state.copy()

	def copy(self):
		b = Board()
		b.state = self.state.copy()
		return b

	def player(self,c):
		self.update("yellow", c)
		self.eval()
		print(self)
		m = 0
		if (self.bot_step != None):
			m = minimax(self)
			print(m[0])
			self.update("red", m[1])
		else:
			m = minimax(self)
			self.update("red", m[1])
		self.eval()
		print(self)


b=Board()
print(b)
while(True):
	x = input()
	b.player(int(x))
#b.update("red", 3)
#b.update("red", 2)
#b.update("red", 4)
#b.update("yellow", 6)
#b.update("yellow", 6)
#b.update("yellow", 6)
print(minimax(b))
# b.player(0)
