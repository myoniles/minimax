#ifndef QUEEN_H
#define QUEEN_H

#include "piece.h"

class Queen: public Piece {
	public:
		Queen();
		Queen(Color c);
		Position* get_possible_moves();
};


#endif
