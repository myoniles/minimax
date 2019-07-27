#ifndef PAWN_H
#define PAWN_H

#include "piece.h"

class Pawn: public Piece {
	public:
		Pawn();
		Pawn(Color c);
		Position* get_possible_moves();
};


#endif
