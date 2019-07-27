#ifndef PIECE
#define PIECE

#include "piece.h"

Piece::Piece( char symbol, int value, Color color ) {
	this->symbol = symbol;
	this->value = value;
	this->color = color;
}

Piece::Piece( char symbol, int value ) {
	this->symbol = symbol;
	this->value = value;
}

// Getters
char Piece::get_symbol() { return this->symbol; };
int Piece::get_value() { return this->value; };
Position Piece::get_position() { return this->currentPosition; };
Color Piece::get_color() { return this->color; };

void Piece::set_position( Position position ) {
	this->currentPosition = position;
}

void Piece::set_position( char x_pos, int y_pos) {
	Position p;
	p.x_pos = x_pos;
	p.y_pos = y_pos;
}

#endif

