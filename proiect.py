import numpy as np
import random


ROWS, COLS = 11, 11

# 0- empty 1-red 2-yellow 3-green 4-blue
CANDY_TYPES = [1, 2, 3, 4]


def initialize_board(rows, cols):
    board = np.zeros((rows, cols), dtype=int)
    for i in range(rows):
        for j in range(cols):
            board[i][j] = random.choice(CANDY_TYPES)
    return board


# Detecting 3 in a row
def detect_three_in_a_row(board):
    score = 0
    to_remove = set()  # we put all the sets that needs to be removed

    for i in range(ROWS): #horizontal check
        for j in range(COLS - 2):
            if board[i][j] == board[i][j + 1] == board[i][j + 2] != 0:
                to_remove.update([(i, j), (i, j + 1), (i, j + 2)])
                score += 5

    for j in range(COLS): #vertical check
        for i in range(ROWS - 2):
            if board[i][j] == board[i + 1][j] == board[i + 2][j] != 0:
                to_remove.update([(i, j), (i + 1, j), (i + 2, j)])
                score += 5

    #eliminate the sets from the board
    for (i, j) in to_remove:
        board[i][j] = 0

    return score, to_remove


#updating the board
def update_board(board):
    for j in range(COLS):
        #from bottom to the top
        for i in range(ROWS - 1, -1, -1):
            if board[i][j] == 0:  # if we find an empty space
                #we search for a candy that s not empty
                for k in range(i - 1, -1, -1):
                    if board[k][j] != 0:
                        board[i][j] = board[k][j]
                        board[k][j] = 0
                        break
                else:

                    board[i][j] = random.choice(CANDY_TYPES)



def print_board(board):
    print("\n".join(["\t".join(map(str, row)) for row in board]))
    print("-" * 40)



def play_game():
    board = initialize_board(ROWS, COLS)
    total_score = 0
    steps = 0

    print("Initial board:")
    print_board(board)

    while steps < 10000:
        score, removed = detect_three_in_a_row(board)
        if not removed:
            break
        total_score += score
        update_board(board)

        print(f"\nAfter step {steps + 1}, score: {total_score}")
        print_board(board)

        steps += 1

    return total_score
def simulate_games(num_games=100):
    scores=[]
    for i in range(num_games):
        score = play_game()
        scores.append(score)
        print(f"Game {i + 1} reached a {score} score!")

    avg_score = sum(scores) / num_games
    print(f"\nAverage score {avg_score}")


if __name__ == "__main__":
   simulate_games(100)
