"""
Mode B: if a digit only occurs once within a block, row, or column,
the only possible digit in the cell where it occured is that digit.
(because if any other digit is placed there, a digit will be missing
in a row, block or column)

Example:
[{1 2 3} {1 2 4 5} {1 3 2 5}] -> [{1 2 3} {4} {1 3 2 5}]
"""

from util import all_digits, containers

def mode_b(board, i, j):
    # {1, 5} {1, 2, 5}, {1, 3, 5} -> {1, 5} {2} {3}
    for c in containers(board, i, j):
        remove_b(c)

def remove_b(sets):
    seen = set()
    seen_twice_or_more = set()
    for set_ in sets:
        for d in set_:
            if d in seen:
                seen_twice_or_more.add(d)
            seen.add(d)

    digits_that_only_occur_once = all_digits() - seen_twice_or_more

    for set_ in sets:
        x = digits_that_only_occur_once & set_
        if x: # x = {digit}
            set_ &= x
