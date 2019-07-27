#ifndef ROOK
#define ROOK

#include "rook.h"
#include "piece.h"

Rook::Rook( Color c ): Piece('R', 5, c){}
Rook::Rook( ): Piece('R', 5){}

Position* Rook::get_possible_moves() {return NULL;}

#endif
