#ifndef KNIGHT_DEF
#define KNIGHT_DEF

#include "piece.h"

class Knight: public Piece {
	public:
		Knight();
		string* get_possible_moves();
};


#endif
