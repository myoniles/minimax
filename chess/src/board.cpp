#ifndef BOARD
#define BOARD

#include <vector>

#include "piece.h"
#include "board.h"

Board::Board(){
	//this->pieces_in_play = new std::vector<Piece>();
}

Position* Board::get_possible_moves() {return NULL; }

int Board::evaluate() {
	int score = 0;
	for (Piece* p: pieces_in_play) {
		int multiplyer = (p->get_color() == white) ? 1 : -1;
		score += multiplyer * p->get_value();
	}
}

#endif

