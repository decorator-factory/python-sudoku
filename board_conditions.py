from util import all_digits, containers, get_singles, unique
from indices import indices

def is_board_wrong(board):
    for i, j in indices():
        if len(board[i][j]) == 0:
            return True
        for c in containers(board, i, j):
            singles = get_singles(c)
            if len(singles) != len([*unique(singles)]):
                return True
    return False

def is_board_complete(board):
    for i, j in indices():
        if len(board[i][j]) != 1:
            return False
    return True