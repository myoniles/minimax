#ifndef KING_DEF
#define KING_DEF

#include "piece.h"

class King: public Piece {
	public:
		King();
		string* get_possible_moves();
};

#endif
