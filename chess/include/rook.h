#ifndef ROOK_DEF
#define ROOK_DEF

#include "piece.h"

class Rook: public Piece {
	public:
		Rook();
		string* get_possible_moves();
};


#endif
