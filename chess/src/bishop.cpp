#ifndef BISHOP
#define BISHOP

#include "bishop.h"
#include "piece.h"

Bishop::Bishop(): Piece('B', 3){}

Position* Bishop::get_possible_moves() {return NULL;}

#endif

