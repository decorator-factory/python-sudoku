"""
Mode A: if there is a cell where only one digit is possible,
no other cell in its row, column or block can contain that digit

Example:
[{1 2 3} {4 5 6} {4} {3 4 5}] -> [{1 2 3} {5 6} {4} {3 5}]
"""

from util import get_singles, union, containers

def remove_a(sets):
    singles = union(get_singles(sets))
    for set_ in sets:
        if len(set_) != 1:
            set_ -= singles

def mode_a(board, i, j):
    # {1, 2, 3} {3} -> {1, 2} {3}
    for c in containers(board, i, j):
        remove_a(c)