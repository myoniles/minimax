
class Board:

    #
    __won = False

    def __init__(self):
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    # used to change the state of the board
    def changeState(self, xpos, ypos, char):
        if (self.board[xpos][ypos] != ' '):
            return False
        else:
            self.board[xpos][ypos]=char
            return True

    # Prints the current board state with vertical bars
    def toString(self):
        counter = 0
        print("  0 1 2")
        for row in self.board:
            print(counter, end=" ", sep="")
            print(row[0], row[1], row[2], sep='|')
            counter +=1

    def readSpot(self, xPos, yPos):
        return self.board[xPos][yPos]
    # returns true if the specific character has more than three in a row
    # this may be vertical, horizontal, and/or diagonal
    def isWon(self, char):
        isWon = False
        winCase = '' + char*3

        for i in self.board:
            if( ''.join(i)== winCase):
                isWon = True

        for k in range(0,3):
            col = ''
            for j in range(0,3):
                col = col + (self.board[j][k])
            if (col == winCase):
                isWon = True

        diag = self.board[0][0]+ self.board[1][1]+ self.board[2][2]
        if (diag == winCase): isWon = True

        diag = self.board[0][2] + self.board[1][1] + self.board[2][0]
        if (diag == winCase): isWon = True

        #if(isWon):
            #print(char, "wins!")

        return isWon

    #prompts the user of an undisclosed character to enter the positions and then write to the board
    def promptUser(self, char):
        xpos = input("May the user, please enter the x coordinate of the letter:")
        ypos = input("May the user, please enter the y coordinate of the letter:")
        if(not self.changeState(int(ypos), int(xpos), char)):
            print("Try again")
            self.promptUser(char)

    # runs a game between two real people
    def run_2p_game(self):
        while(not self.__won):
            print(self.toString())
            self.promptUser('o')

            if (self.isWon('o')):
                self.__won = True
                break;

            print(self.toString())
            self.promptUser('x')

            if (self.isWon('x')):
                print(self.toString())
                self.__won = True

    def isFull(self):
        counter = 0
        for i in self.board:
            for j in i:
                if (j == ' '):
                    counter += 1
        if(counter == 9):
            return True
        else:
            return False


    def getMoves(self):
        moves = []
        for row in range(0,3):
            for col in range(0,3):
                move = []
                if( self.board[row][col] == ' '):
                    move.append(row)
                    move.append(col)
                    moves.append(move)
        return moves

    def equalized(self, b):
        for i in range (0,3):
            for j in range (0,3):
                self.board[i][j] = b.board[i][j]



