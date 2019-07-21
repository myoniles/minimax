#include <string>

using namespace std;

class	Piece {
	public:
		Piece( char symbol ) {
			this->symbol = symbol;
		}

		virtual string* get_possible_moves();
		virtual char get_symbol();
		~Piece();
	protected:
		char symbol;
};
