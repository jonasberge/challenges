# https://www.codewars.com/kata/529bf0e9bdf7657179000008

N = 9
S = 3

class Sudoku:
    def __init__(self, board):
        self.board = board

    def row(self, i):
        return self.board[i]

    def column(self, i):
        return [row[i] for row in self.board]

    def square(self, i):
        x, y = i % S, i // S
        x, y = x * S, y * S
        return [
            self.board[y + u][x + v]
            for u in range(S)
            for v in range(S)
        ]

def valid_chunk(chunk):
    chunk = set(chunk)
    return len(chunk) == N and 0 not in chunk

def valid_solution(board):
    sudoku = Sudoku(board)
    for i in range(9):
        if not all([
            valid_chunk(sudoku.row(i)),
            valid_chunk(sudoku.column(i)),
            valid_chunk(sudoku.square(i)),
        ]): return False
    return True
