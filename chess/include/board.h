#ifndef BOARD_H
#define BOARD_H

#include <string>

class Board {
	public:
		Board();
		Position* get_possible_moves();
		int evaluate();
	private:
		Piece* pieces_in_play;
};

#endif

