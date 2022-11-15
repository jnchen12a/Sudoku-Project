# Useful for debugging and checking if modules work
from sudoku_generator import SudokuGenerator

sudoku = SudokuGenerator(9, 0)
print(sudoku.valid_in_col(1, 0))
print(sudoku.valid_in_box(3, 3, 6))
sudoku.print_board()