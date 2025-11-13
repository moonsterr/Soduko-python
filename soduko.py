import random

class Sudoku(object):
    SIZE = 9  
    EMPTY = '.'  

    def __init__(self):
        self.board = [[Sudoku.EMPTY for _ in range(Sudoku.SIZE)] for _ in range(Sudoku.SIZE)]
        self.lives = 3
        self.history = []
        self.gamestarted = False

    def get_board(self):
        lines = []
        for i, row in enumerate(self.board):
            line = ''
            for j, cell in enumerate(row):
                line += cell + ' '
                if (j + 1) % 3 == 0 and j != Sudoku.SIZE - 1:
                    line += '| '
            lines.append(line.strip())
            if (i + 1) % 3 == 0 and i != Sudoku.SIZE - 1:
                lines.append('-' * 21)
        return '\n'.join(lines)
    
    def set_cell(self, row,col,n):
        if not self.verify_numbers(row,col,n):
            if self.gamestarted:
                print(f"Invalid input: row {row}, col {col}, value {n}")
            return
        if not self.is_valid_move(row, col, n):
            self.lives -= 1
            if self.gamestarted:
                print(f"Invalid move! Number {n} already in row, column, or block. Lives left: {self.lives}")
            return

        self.board[row][col] = str(n)
        self.history.append((row, col, n))
    def verify_numbers(self, row,col,n):
        row_col = [0,1,2,3,4,5,6,7,8]
        numbers = [1,2,3,4,5,6,7,8,9]
        veri_row = row in row_col
        veri_col = col in row_col
        veri_n = n in numbers
        return veri_col and veri_n and veri_row

    def is_valid_move(self, row, col, n):
        n_str = str(n)
        if n_str in self.board[row]:
            return False
        if n_str in [self.board[r][col] for r in range(Sudoku.SIZE)]:
            return False
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for r in range(start_row, start_row + 3):
            for c in range(start_col, start_col + 3):
                if self.board[r][c] == n_str:
                    return False
        return True
    def remaining_lives(self):
        return self.lives
    def setup_board(self):
        for i in range(30):
            num = random.randint(1,9)
            col = random.randint(0,8)
            row = random.randint(0,8)
            self.set_cell(row=row,col=col,n=num)
        self.gamestarted = True
    
