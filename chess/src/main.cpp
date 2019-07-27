#include <stdio.h>

#include "bishop.h"
#include "king.h"
#include "knight.h"
#include "pawn.h"
#include "queen.h"
#include "rook.h"
#include "board.h"

int main(){
	Piece* p1 = new Bishop();
	Piece* p2 = new King();
	Piece* p3 = new Knight();
	Piece* p4 = new Pawn();
	Piece* p5 = new Queen();
	Piece* p6 = new Rook();
	printf("%c\n", p1->get_symbol());

	Board board;
	Player player1(white);
	Player player2(black);
	board.initialize_game( player1, player2 );
}
