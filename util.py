from indices import indices_functions

def unique(iterable):
    seen = []
    for i in iterable:
        if i not in seen:
            yield i
            seen.append(i)

def all_digits():
    return {1, 2, 3, 4, 5, 6, 7, 8, 9}

def from_indices(board, indices):
    return [board[i][j] for i, j in indices]

def containers(board, i, j):
    for indf in indices_functions:
        yield from_indices(board, indf(i, j))

def get_singles(sets):
    # [{1, 2, 3}, {5}, {6}, {7, 8}] -> [{5}, {6}]
    return [set_ for set_ in sets if len(set_) == 1]

def union(sets):
    # [{1, 2}, {3}, {3, 4}] -> {1, 2, 3, 4}
    result = set()
    for set_ in sets:
        result |= set_
    return result