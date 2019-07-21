#ifndef QUEEN_DEF
#define QUEEN_DEF

#include "piece.h"

class Queen: public Piece {
	public:
		Queen();
		string* get_possible_moves();
};


#endif
