#ifndef PAWN_H
#define PAWN_H

#include "piece.h"

class Pawn: public Piece {
	public:
		Pawn();
		Position* get_possible_moves();
};


#endif
