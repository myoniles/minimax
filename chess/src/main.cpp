#include <stdio.h>

#include "bishop.h"
#include "king.h"
#include "knight.h"
#include "pawn.h"
#include "queen.h"
#include "rook.h"

int main(){
	Piece* p1 = new Bishop();
	Piece* p2 = new King();
	Piece* p3 = new Knight();
	Piece* p4 = new Pawn();
	Piece* p5 = new Queen();
	Piece* p6 = new Rook();
	printf("%c\n", p1->get_symbol());
}
