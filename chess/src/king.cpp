#ifndef KING
#define KING

#include "king.h"
#include "piece.h"

King::King( Color c ): Piece('K', 100, c){}
King::King( ): Piece('K', 100){}

Position* King::get_possible_moves() {return NULL;}

#endif

