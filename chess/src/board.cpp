#ifndef BOARD
#define BOARD

#include <vector>

#include "piece.h"
#include "board.h"
#include "bishop.h"
#include "king.h"
#include "knight.h"
#include "pawn.h"
#include "queen.h"
#include "rook.h"
#include "board.h"

Board::Board() { }

Position* Board::get_possible_moves() {return NULL; }

/*
This function is the one that will have a greatest impact on performance.
Right now we are summing the values of pieces on the board, but I think this has room for improvement.
*/
int Board::evaluate() {
	int score = 0;
	for (Piece* p: pieces_in_play) {
		int multiplyer = (p->get_color() == white) ? 1 : -1;
		score += multiplyer * p->get_value();
	}
	return score;
}

void initialize_player( Color c, vector<Piece*>* pieces_in_play ) {
	int front_row, back_row;

	switch ( c ) {
		case white:
			front_row = 2;
			back_row = 1;
			break;
		case black:
			front_row = 7;
			back_row = 8;
			break;
	}

	for ( char i = 'a'; i <= 'h'; i++ ){
		Pawn* p = new Pawn( c );
		// Whoever designed chess should have really indexed at 0
		p->set_position( i, front_row );
		pieces_in_play->push_back(p);
	}

	// TODO find a more elegant way to do this
	Rook* r1 = new Rook( c ); r1->set_position( 'a', back_row ); pieces_in_play->push_back(r1);
	Rook* r2 = new Rook( c ); r2->set_position( 'h', back_row ); pieces_in_play->push_back(r2);
	Knight* n1 = new Knight( c ); n1->set_position( 'b', back_row ); pieces_in_play->push_back(n1);
	Knight* n2 = new Knight( c ); n2->set_position( 'g', back_row ); pieces_in_play->push_back(n2);
	Bishop* b1 = new Bishop( c ); b1->set_position( 'c', back_row ); pieces_in_play->push_back(b1);
	Bishop* b2 = new Bishop( c ); b2->set_position( 'f', back_row ); pieces_in_play->push_back(b2);
	King* k = new King( c ); k->set_position( 'e', back_row ); pieces_in_play->push_back(k);
	Queen* q = new Queen( c ); q->set_position( 'd', back_row ); pieces_in_play->push_back(q);
}

void Board::initialize_game( Player white_player, Player black_player ) {
	initialize_player( white_player.get_color(), &pieces_in_play);
	initialize_player( black_player.get_color(), &pieces_in_play);

}

#endif
