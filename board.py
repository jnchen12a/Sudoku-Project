# Board Class
# FIXME: Finish the rest of this class
from constants import *
import pygame
class Board:
  def __init__(self, width, height, screen, difficulty):
    self.width = width
    self.height = height
    self.screen = screen
    self.difficulty = difficulty
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

  def clear(self):
    pass
    
  def sketch(self, value):
      pass

  def place_number(self, value):
    pass

  def reset_to_original(self):
    pass

  def is_full(self):
    pass

  def update_board(self):
    pass

  def find_empty(self):
    pass

  def check_board(self):
    pass