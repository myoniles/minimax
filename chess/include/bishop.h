#ifndef BISHOP_H
#define BISHOP_H

#include "piece.h"

class Bishop: public Piece {
	public:
		Bishop();
		Bishop(Color c);
		Position* get_possible_moves();
};

#endif
