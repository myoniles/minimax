#ifndef BISHOP
#define BISHOP

#include "bishop.h"
#include "piece.h"

Bishop::Bishop( Color c ): Piece('B', 3, c){}
Bishop::Bishop( ): Piece('B', 3){}

Position* Bishop::get_possible_moves() {return NULL;}

#endif

