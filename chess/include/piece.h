#ifndef PIECE_H
#define PIECE_H

#include <string>

using namespace std;

typedef struct Position {
	// this is done from WHITE's perspective
	int x_pos;
	char y_pos;
} Position;

enum Color { white, black };

class	Piece {
	public:
		Piece( char symbol, int value, Color color);
		Piece( char symbol, int value);
		virtual Position* get_possible_moves() = 0;
		char get_symbol();
		int get_value();
		Position get_position( );
		Color get_color( );
		void set_position( Position position );
		void set_position( char x_pos, int y_pos);
		~Piece(){};

	protected:
		char symbol;
		int value;
		Position currentPosition;
		Color color;

		// private because we might want to be able to declare pieces w/o color
		void set_color();
};

#endif
