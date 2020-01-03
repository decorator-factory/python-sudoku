def indices():
    for i in range(9):
        for j in range(9):
            yield i, j

def row_indices(i, j):
    for x in range(9):
        yield (i, x)

def col_indices(i, j):
    for x in range(9):
        yield (x, j)

def blk_indices(i, j):
    i -= i%3
    j -= j%3
    for a in range(3):
        for b in range(3):
            yield (i+a, j+b)

indices_functions = (row_indices, col_indices, blk_indices)
