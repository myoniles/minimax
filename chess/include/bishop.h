#ifndef BISHOP_DEF
#define BISHOP_DEF

#include "piece.h"

class Bishop: public Piece {
	public:
		Bishop();
		string* get_possible_moves();
};

#endif
