# python-sudoku
Sudoku solver in python

## Usage

```
python3 main.py
```

See `in.txt`.
Output is formatted nicely in HTML:

![Output example](https://i.imgur.com/9iDBz8C.png)

## Reasoning modes

This solver uses three modes of reasoning that are used in `sgt-puzzles/solo`

A.
```
- Numeric elimination: a square must have a particular number
  in because all the other numbers that could go in it are
  ruled out.
```

B.

```
- Positional elimination: a number must go in a particular
  square because all the other empty squares in a given
  row/col/blk are ruled out.
```

C
```
 - Recursion. If all else fails, we pick one of the currently
   most constrained empty squares and take a random guess at its
   contents, then continue solving on that basis and see if we
   get any further.
```
