#ifndef KING_H
#define KING_H

#include "piece.h"

class King: public Piece {
	public:
		King();
		Position* get_possible_moves();
};

#endif
