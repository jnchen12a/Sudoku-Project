# Useful for debugging and checking if modules work
from sudoku_generator import SudokuGenerator
from sudoku_generator import generate_sudoku
'''
board = generate_sudoku(9, 50)
for index, row in enumerate(board):
          count = 0
          count_2 = 0
          for number in row:
            print(number, end=' ')
            count += 1
            count_2 += 1
            if count == 3:
              print('|', end=' ')
              count = 0
            if count_2 == 9:
              print()

          if (index + 1) % 3 == 0:
            print("-" * 23)
print()
'''
sudoku = SudokuGenerator(9, 30)
sudoku.fill_values()
board = sudoku.get_board()
sudoku.remove_cells()
board = sudoku.get_board()
for index, row in enumerate(board):
          count = 0
          count_2 = 0
          for number in row:
            print(number, end=' ')
            count += 1
            count_2 += 1
            if count == 3:
              print('|', end=' ')
              count = 0
            if count_2 == 9:
              print()

          if (index + 1) % 3 == 0:
            print("-" * 23)
print(sudoku.is_valid(0, 3, 1))
print(sudoku.row_length)
print(sudoku.box_length)
print(sudoku.get_board()[3][3])