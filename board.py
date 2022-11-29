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

  def select(self, row, col):
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

  def check_board(self):
    pass