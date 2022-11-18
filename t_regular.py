# Useful for debugging and checking if modules work
from sudoku_generator import SudokuGenerator
from sudoku_generator import generate_sudoku

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