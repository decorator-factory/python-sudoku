"""
Mode C: 

"""

from copy import deepcopy
from indices import indices

def unsolved_index(board):
    # find the first index of an unsolved cell,
    # searching through cells with 2 choices, then
    # 3 choices, then 4 choices and so on
    for n in range(2, 9):
        for i, j in indices(): 
            if len(board[i][j]) == n:
                return (i, j)

def with_cell_replaced(board, i, j, digit):
    new_board = deepcopy(board)
    new_board[i][j] = {digit}
    return new_board

def mode_c(board, solve_function):
    i, j = unsolved_index(board)
    set_ = board[i][j]
    for digit in set_:
        new_board = with_cell_replaced(board, i, j, digit)
        solved = solve_function(new_board)
        if solved is not None:
            return solved
    return None