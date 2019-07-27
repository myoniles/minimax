#ifndef QUEEN
#define QUEEN

#include "queen.h"
#include "piece.h"

Queen::Queen( Color c ): Piece('Q', 9, c){}
Queen::Queen( ): Piece('Q', 9){}

Position* Queen::get_possible_moves() {return NULL;}

#endif

