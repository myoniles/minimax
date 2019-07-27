#ifndef KING
#define KING

#include "king.h"
#include "piece.h"

King::King(): Piece('K', 100){}

Position* King::get_possible_moves() {return NULL;}

#endif

