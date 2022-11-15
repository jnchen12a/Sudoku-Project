# Useful for debugging and checking if modules work
from sudoku_generator import SudokuGenerator

sudoku = SudokuGenerator(9, 0)
print(sudoku.is_valid(0, 0, 3))
sudoku.print_board()