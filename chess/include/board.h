#ifndef BOARD_H
#define BOARD_H

#include <string>
#include <vector>

class Board {
	public:
		Board();
		Position* get_possible_moves();
		int evaluate();
	private:
			vector<Piece*> pieces_in_play;
	};

#endif

