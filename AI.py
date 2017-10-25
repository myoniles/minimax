# AI Begins
from board import Board

def evaluate_face_Board(b):
    b_value = None
    if (b.isWon('x')):
        b_value = 1
    elif (b.isWon('o')):
        b_value = -1
    elif(b.isFull()):
        b_value = 0
    return b_value

def minimax(b):
    moves = b.getMoves()
    best = moves[0]
    best_score = -100000
    for move in moves:
        temp = Board()
        temp.equalized(b)
        temp.changeState(move[0], move[1], 'x')
        score = min(temp)
        if score > best_score:
            best = move
            best_score = score
    return best

    #for




def min(b):
    if(b.isWon('x') or b.isWon('o')):
        return evaluate_face_Board(b)
    moves = b.getMoves()
    best = moves[0]
    best_score = 100000
    for move in moves:
        temp = Board()
        temp.equalized(b)
        temp.changeState(move[0], move[1], 'o')
        score = max(temp)
        if score < best_score:
            best_score = score
    return best_score

def max(b):
    if(b.isWon('x') or b.isWon('o')):
        return evaluate_face_Board(b)
    moves = b.getMoves()
    best_score = -100000
    for move in moves:
        temp = Board()
        temp.equalized(b)
        temp.changeState(move[0], move[1], 'x')
        score = max(temp)
        if score > best_score:
            best = move
            best_score = score
    return best_score

#print(heck.toString())
#print(evaluate_deep(heck,0))

def AI_turn(b):
    move = minimax(b)

    b.changeState(move[0], move[1], 'x')
    return b

def play_AI_game(b):
    won = False
    while (not won):
        print(b.toString())
        b.promptUser('o')

        if (b.isWon('o')):
            won = True
            break;

        print(b.toString())
        AI_turn(b)


        if (b.isWon('x')):
            print(b.toString())
            won = True

heck = Board()
play_AI_game(heck)