#ifndef PAWN_DEF
#define PAWN_DEF

#include "piece.h"

class Pawn: public Piece {
	public:
		Pawn();
		string* get_possible_moves();
};


#endif
