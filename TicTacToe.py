import random
import time

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    bd = []
    top_row = 3*("+" + 7 * "-") + "+"
    empty_row = 3*("|" + 7 * " ") + "|"
    for line in board:
        bd.append(top_row)
        bd.append(empty_row)
        num_line = ""
        for column in line:
            num_line += "|   " + str(column) + "   "
        num_line += "|"
        bd.append(num_line)
        bd.append(empty_row)
    bd.append(top_row)
    print('\n'.join(bd))
        

def enter_move(board):
    move = False
    while move == False:
        try:
            pos = int(input("Enter position to place your piece (O):"))
            for i, row in enumerate(board):
                if pos in row:
                    board[i][row.index(pos)] = "O"
                    move = True
            if move == False:
                print("Invalid move")
        except:
            print("Invalid move")
    display_board(board)
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.


def make_list_of_free_fields(board):
    free_fields = []
    for row_index, row in enumerate(board):
        for col_index, square in enumerate(row):
            if square != "O" and square != "X":
                free_fields.append((row_index, col_index))
    return free_fields
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.


def victory_for(board, sign):
    for row in board:
        if row[0] == sign and row[1] == sign and row[2] == sign:
            return True
    for column in range(3):
        if board[0][column] == sign and board[1][column] == sign and board[2][column] == sign:
            return True
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    if board[2][0] == sign and board[1][1] == sign and board[0][2] == sign:
        return True
    return False
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game


def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    if not free_fields:
        print("Game over: no winner")
        return False
    time.sleep(1)
    print("Computer's move (X):")
    random_field = random.choice(free_fields)
    board[random_field[0]][random_field[1]] = "X"
    display_board(board)
    return True
    # The function draws the computer's move and updates the board.

board = [[1,2,3], [4,5,6], [7,8,9]]
display_board(board)
while True:
    enter_move(board)
    if victory_for(board, "O") == True:
        print("Game over: Player wins!")
        break
    if draw_move(board) == False:
        break
    if victory_for(board, "X") == True:
        print("Game over: Computer wins!")
        break
