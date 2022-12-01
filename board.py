# Board Class
# FIXME: Finish the rest of this class
from constants import *
from cell import Cell
import pygame
class Board:
  def __init__(self, width, height, screen, difficulty, original):
    self.width = width
    self.height = height
    self.screen = screen
    self.difficulty = difficulty
    self.original = original
  def draw(self):
    # Horizontal lines
    count = 1
    for i in range(10):
      LINE_WIDTH = BOLD_WIDTH if count == 1 else THIN_WIDTH
      pygame.draw.line(self.screen, BLACK, (0, SQUARE_SIZE * i), (WIDTH, SQUARE_SIZE * i), LINE_WIDTH)
      if count == 3:
        count = 1
      else:
        count += 1

    # Vertical lines
    count = 1
    for i in range(10):
      LINE_WIDTH = BOLD_WIDTH if count == 1 else THIN_WIDTH
      pygame.draw.line(self.screen, BLACK, (SQUARE_SIZE * i, 0), (SQUARE_SIZE * i, BOARD_LENGTH), LINE_WIDTH)
      if count == 3:
        count = 1
      else:
        count += 1

  def select(self, row, col, removed_cells):
    if row == None:
      return
    if col == None:
      return
    if row > 9:
      return
    id = (row * 9) + col
    if id not in removed_cells:
      return
    start_coordinate_top = ((SQUARE_SIZE * col) + 4, (SQUARE_SIZE * row) + 4)
    end_coordinate_top = ((SQUARE_SIZE * (col + 1)) - 4, (SQUARE_SIZE * row) + 4)
    start_coordinate_bottom = ((SQUARE_SIZE * col) + 4, (SQUARE_SIZE * (row + 1)) - 4)
    end_coordinate_bottom = ((SQUARE_SIZE * (col + 1)) - 4, ((SQUARE_SIZE * (row + 1)) - 4))

    # Horizontal lines
    pygame.draw.line(self.screen, RED, start_coordinate_top, end_coordinate_top, HIGHLIGHT_WIDTH)
    pygame.draw.line(self.screen, RED, start_coordinate_bottom, end_coordinate_bottom, HIGHLIGHT_WIDTH)

    # Vertical lines
    pygame.draw.line(self.screen, RED, start_coordinate_top, start_coordinate_bottom, HIGHLIGHT_WIDTH)
    pygame.draw.line(self.screen, RED, end_coordinate_top, end_coordinate_bottom, HIGHLIGHT_WIDTH)

  def click(self, x, y):
    x = x // SQUARE_SIZE
    if y > 450:
      return None
    else:
      y = y // SQUARE_SIZE

    return (x, y)

  def clear(self, cell, removed_cells):
    id = (cell.row * 9) + (cell.col * 9)
    if id in removed_cells:
      return None
    else:
      cell.set_cell_value(0)
      return True
    
  def place_number(self, value):
    pass

  def reset_to_original(self, cell_list):
    for row_num, row in enumerate(cell_list):
      for col_num, cell in enumerate(row):
        cell.set_cell_value(self.original[row_num][col_num])

    return True

  def is_full(self, cell_list):
    for row in cell_list:
      for cell in row:
        if cell.value == 0:
          return False

    return True
  def update_board(self): # Don't need?
    pass

  def find_empty(self): # Don't need?
    pass

  def valid_in_row(self, row, num, cell_list):
    count = 0
    for cell in cell_list[row]:
      if num == cell.value:
        count += 1
    if count == 1:
      return True
    else:
      return False

  def valid_in_col(self, col, num, cell_list):
    count = 0
    for board_row in cell_list: # Loops through each row
      if board_row[int(col)].value == num: # Checks if column matching index contains num
        count += 1
    if count == 1:
      return True
    else:
      return False

  def valid_in_box(self, row_start, col_start, num, cell_list):
    count = 0
    for row in range(row_start, row_start + 3):
      for column in range(int(col_start), int(col_start + 3)):
        if cell_list[row][column].value == num:
          count += 1
    if count == 1:
      return True
    else:
      return False

  def check_board(self, cell_list): # False if it is incorrect, True if it is correct
    for row_num, row in enumerate(cell_list):
      for col_num, cell in enumerate(row):
        num = cell.value
        row_start = int(row_num // 3) * 3
        col_start = int(col_num // 3) * 3
        if self.valid_in_row(row_num, num, cell_list) and self.valid_in_col(col_num, num, cell_list) and self.valid_in_box(row_start, col_start, num, cell_list):
          pass
        else:
          return False

    return True