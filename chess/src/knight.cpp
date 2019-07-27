#ifndef KNIGHT
#define KNIGHT

#include "knight.h"
#include "piece.h"

Knight::Knight( Color c ): Piece('N', 3, c){}
Knight::Knight( ): Piece('N', 3){}

Position* Knight::get_possible_moves() {return NULL;}

#endif

