from soduko import Sudoku

sudoku_board = Sudoku()
print(sudoku_board.get_lives())
while sudoku_board.remaining_lives() > 0:
    print(sudoku_board.get_board())
    try:
        input_str = input("Enter row/col/number (0-8/0-8/1-9): ")
        row, col, n = map(int, input_str.split('/'))
    except ValueError:
        print("Invalid format! Use row/col/number, e.g., 2/3/5")
        continue
    if row not in range(9) or col not in range(9) or n not in range(1, 10):
        print("Values out of range!")
        continue

    sudoku_board.set_cell(row, col, n)
    print(sudoku_board.get_board())
    print(sudoku_board.history)
print('hi')