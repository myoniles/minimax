#ifndef BOARD_H
#define BOARD_H

#include <string>
#include <vector>

#include "player.h"
#include "bishop.h"
#include "king.h"
#include "knight.h"
#include "pawn.h"
#include "queen.h"
#include "rook.h"
#include "board.h"

class Board {
	public:
		Board();
		Position* get_possible_moves();
		int evaluate();
		void initialize_game( Player white_player, Player black_player );
	private:
			vector<Piece*> pieces_in_play;
	};

#endif

