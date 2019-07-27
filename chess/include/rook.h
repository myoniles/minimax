#ifndef ROOK_H
#define ROOK_H

#include "piece.h"

class Rook: public Piece {
	public:
		Rook();
		Rook(Color c);
		Position* get_possible_moves();
};


#endif
