from copy import deepcopy

from _sudoku_html import html

from indices import indices
from util import all_digits

from mode_a import mode_a
from mode_b import mode_b
from mode_c import mode_c

from board_conditions import is_board_complete, is_board_wrong


def solve(board):
    while True:
        new_board = deepcopy(board)
        for i, j in indices():
            mode_a(new_board, i, j)
        for i, j in indices():
            mode_b(new_board, i, j)
        if new_board == board:
            break
        board = new_board

    if is_board_complete(board):
        return board

    if is_board_wrong(board):
        return None

    return mode_c(board, solve)


#####

with open("in.txt") as file:
    board = []
    for line in file:
        numbers = [int(s) for s in line.split()]
        row = [{n} if n > 0 else all_digits() for n in numbers]
        board.append(row)

html(solve(board), "out.html")