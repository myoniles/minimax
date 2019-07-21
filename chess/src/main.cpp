#include <stdio.h>

#include "bishop.h"
#include "king.h"
#include "knight.h"
#include "pawn.h"
#include "queen.h"
#include "rook.h"

int main(){
	Piece* p = new Rook();
	printf("%c\n", p->get_symbol());
}
