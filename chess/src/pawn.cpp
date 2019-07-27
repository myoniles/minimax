#ifndef PAWN
#define PAWN

#include "pawn.h"
#include "piece.h"

Pawn::Pawn( Color c ): Piece('P', 1, c){}
Pawn::Pawn( ): Piece('P', 1){}

Position* Pawn::get_possible_moves() {return NULL;}

#endif

