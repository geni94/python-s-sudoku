from __future__ import print_function

VALS = range(1, 10)

def is_finished(board):
    #returns the number of cells that still have multiple possibilities
    for i in range(9):
        for j in range(9):
            if not board[i][j]:
                return False
    return True

def get_square(i):
    if 0 <= i < 3:
        return [0, 1, 2]
    elif 3 <= i < 6:
        return [3, 4, 5]
    else:
        return [6, 7, 8]

def get_cell_square(board, i, j):
    lines = get_square(i)
    cols = get_square(j)
    values = []
    for x in lines:
        for y in cols:
            values.append(board[x][y])
    return values

def column_ok(board, col, value):
    #count number of times that value occurs into the candidates
    for i in range(9):
        if board[i][col] == value:
            return False
    return True

def line_ok(board, line, value):
    # this True if the square to which cell (i, j) belong doesn't contain <value>

    for j in range(9):
        if board[line][j] == value:
            return False
    return True

def square_ok(board, i, j, value):
    # True if the square to which cell (i, j) belong doesn't contains <value>.
    for cell in get_cell_square(board, i, j):
        if cell == value:
            return False
    return True

def is_ok(board, i, j, value):
    #Detect if the cell (i, j) can take the value <value> without breaking any constraints

    if line_ok(board, i, value):
        if column_ok(board, j, value):
            if square_ok(board, i, j, value):
                return True
    return False

def get_copy(board):
    nboard = []
    for i in range(9):
        nboard.append(range(1, 10))
    for i in range(9):
        for j in range(9):
            nboard[i][j] = board[i][j]
    return nboard

def solve(board, solutions):
    if is_finished(board):
        solutions.append(board)
        return None
    else:
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    for val in VALS:
                        if is_ok(board, i, j, val):
                            next_board = get_copy(board)
                            next_board[i][j] = val
                            next_board = solve(next_board, solutions)
                            if next_board != None:
                                return next_board
                    else:
                        return None


def print_board(board):
    for line in board:
        for cell in line:
            print(cell, end=" ")
        print()


#Declaration and init of the board
board = []
for i in range(9):
    board.append(range(1, 10))

for i in range(9):
    for j in range(9):
        board[i][j] = 0

board[0][1] = 1
board[0][5] = 4

board[1][0] = 5
board[1][3] = 1
board[1][8] = 6

board[2][2] = 9
board[2][3] = 8
board[2][5] = 2
board[2][8] = 5

board[3][1] = 6
board[3][4] = 9
board[3][7] = 8

board[5][0] = 4
board[5][1] = 3
board[5][5] = 1
board[5][6] = 7

board[6][4] = 2
board[6][5] = 9
board[6][8] = 1

board[7][0] = 8
board[7][1] = 4
board[7][6] = 9
board[7][8] = 2

board[8][0] = 1
board[8][4] = 4
board[8][7] = 5

solutions = []
solve(board, solutions)
for (i, sol) in enumerate(solutions):
    print("*** Solution number " + str(i + 1) + " ***")
    print_board(sol)