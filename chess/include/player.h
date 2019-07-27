#ifndef PLAYER_H
#define PLAYER_H

#include "piece.h"

class Player {
	public:
		Player( Color color );
		Position* get_possible_moves();
		Color get_color();
		void get_move(Position new_position);
	private:
		Color color;
};

#endif

