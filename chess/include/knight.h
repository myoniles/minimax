#ifndef KNIGHT_H
#define KNIGHT_H

#include "piece.h"

class Knight: public Piece {
	public:
		Knight();
		Knight(Color c);
		Position* get_possible_moves();
};


#endif
