#ifndef PLAYER
#define PLAYER

#include "player.h"

Player::Player( Color color ) {
	this->color = color;
}

Position* Player::get_possible_moves() { return NULL; }

Color Player::get_color() { return this->color; }

void Player::get_move(Position new_position) {
	// TODO
}

#endif

