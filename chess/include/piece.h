#ifndef PIECE_DEF
#define PIECE_DEF

#include <string>

using namespace std;

class	Piece {
	public:
		Piece();
		Piece( char symbol ) { this->symbol = symbol; }
		virtual string* get_possible_moves() = 0;
		char get_symbol() { return this->symbol; };
		~Piece(){};
	protected:
		char symbol;
};

#endif
