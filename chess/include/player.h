#ifndef PLAYER_H
#define PLAYER_H

#include "piece.h"

enum Color { white, black };

class Player {
	public:
		Player( Color color );
		Position* get_possible_moves();
		Color get_color();
	private:
		Color color;
};

#endif

