import pygame
from constants import *
from board import Board
from cell import Cell
from sudoku_generator import SudokuGenerator
from sudoku_generator import generate_sudoku
import sys

def draw_start_screen(screen): # Return number of removed cells
  screen.fill(WHITE)
  font = pygame.font.Font(None, 40)
  title_surf = font.render('Sudoku!', 0, BLACK)
  title_rect = title_surf.get_rect(center=(WIDTH // 2, (SCREEN_LENGTH // 2) - 150))
  screen.blit(title_surf, title_rect)
  while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()
  return 30

def draw_game_screen(screen, board):
  # Use draw() method from Board class

  # Initialize fonts
  font = pygame.font.Font(None, 30)

  #Background Color
  screen.fill(WHITE)

  #Drawing board
  board.draw()

  # Drawing buttons
  # Initializing text
  reset_text = font.render('Reset', 0, WHITE)
  restart_text = font.render('Restart', 0, WHITE)
  exit_text = font.render('Exit', 0, WHITE)
  finish_text = font.render('Finish', 0, WHITE)
  # Initializing background color
  reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
  reset_surface.fill(BLACK)
  reset_surface.blit(reset_text, (10, 10))
  restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
  restart_surface.fill(BLACK)
  restart_surface.blit(restart_text, (10, 10))
  exit_surface = pygame.Surface(((exit_text.get_size()[0] + 20), exit_text.get_size()[1] + 20))
  exit_surface.fill(BLACK)
  exit_surface.blit(exit_text, (10, 10))
  finish_surface = pygame.Surface((finish_text.get_size()[0] + 20, finish_text.get_size()[1] + 20))
  finish_surface.fill(BLACK)
  finish_surface.blit(finish_text, (10, 10))
  # Initializing button rectangle
  reset_rectangle = reset_surface.get_rect(center=(WIDTH // 5, BOARD_LENGTH + 37.5))
  restart_rectangle = restart_surface.get_rect(center=((WIDTH // 5) * 2, BOARD_LENGTH + 37.5))
  exit_rectangle = exit_surface.get_rect(center=((WIDTH // 5) * 3, BOARD_LENGTH + 37.5))
  finish_rectangle = finish_surface.get_rect(center=((WIDTH // 5) * 4, BOARD_LENGTH + 37.5))
  # Drawing buttons
  screen.blit(reset_surface, reset_rectangle)
  screen.blit(restart_surface, restart_rectangle)
  screen.blit(exit_surface, exit_rectangle)
  screen.blit(finish_surface, finish_rectangle)

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if reset_rectangle.collidepoint(event.pos):
          # Reset to original
          print('Reset')
          pass
        if restart_rectangle.collidepoint(event.pos):
          print('Restart')
          pass
        if exit_rectangle.collidepoint(event.pos):
          pygame.quit()
          pass
        if finish_rectangle.collidepoint(event.pos):
          print('Finish')
          pass

    pygame.display.update()

def draw_win_screen(screen):
  # Initialize Title Fonts
  end_title_font = pygame.font.Font(None, 100)
  button_font = pygame.font.Font(None, 70)

  # Background Color
  screen.fill(WHITE)

  # Initialize and Draws Game Won
  end_title_surface = end_title_font.render("Game Won!", 0, BLACK)
  end_rectangle = end_title_surface.get_rect(center=(WIDTH // 2, SCREEN_LENGTH // 2 - 150))
  screen.blit(end_title_surface, end_rectangle)

  # Initialize Button and Text
  exit_text = button_font.render("Exit", 0, BLACK)

  # Initialize Button Background Color and Text
  exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
  exit_surface.fill(RED)
  exit_surface.blit(exit_text, (10, 10))

  # Initialize Button Rectangle
  exit_rectangle = exit_surface.get_rect(center=(WIDTH // 2, SCREEN_LENGTH // 2 + 50))

  # Draws Buttons
  screen.blit(exit_surface, exit_rectangle)

  # While loop waiting for user input
  while True:
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              sys.exit()
          if event.type == pygame.MOUSEBUTTONDOWN:
              if exit_rectangle.collidepoint(event.pos):
                  sys.exit()

      pygame.display.update()

def draw_lost_screen(screen):
   # Initialize Title Fonts
  end_title_font = pygame.font.Font(None, 100)
  button_font = pygame.font.Font(None, 70)

  # Background Color
  screen.fill(WHITE)

  # Initialize and Draws Game Won
  end_title_surface = end_title_font.render("Game Lost", 0, BLACK)
  end_rectangle = end_title_surface.get_rect(center=(WIDTH // 2, SCREEN_LENGTH // 2 - 150))
  screen.blit(end_title_surface, end_rectangle)

  # Initialize Button and Text
  restart_text = button_font.render("Restart", 0, BLACK)

  # Initialize Button Background Color and Text
  restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
  restart_surface.fill(RED)
  restart_surface.blit(restart_text, (10, 10))

  # Initialize Button Rectangle
  restart_rectangle = restart_surface.get_rect(center=(WIDTH // 2, SCREEN_LENGTH // 2 + 50))

  # Draws Buttons
  screen.blit(restart_surface, restart_rectangle)

  # While loop waiting for user input
  while True:
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              sys.exit()
          if event.type == pygame.MOUSEBUTTONDOWN:
              if restart_rectangle.collidepoint(event.pos):
                  return

      pygame.display.update()
    
if __name__ == '__main__':
  pygame.init()
  pygame.display.set_caption('Sudoku') # Title of the window
  screen = pygame.display.set_mode((WIDTH, SCREEN_LENGTH)) # Size of the display

  # After user chooses difficulty
  
  while True: # Event loop
    num_removed_cells = draw_start_screen(screen)
    board, removed_cells = generate_sudoku(9, num_removed_cells)
    original_board = board[:]

    sudoku_board = Board(WIDTH, BOARD_LENGTH, screen, num_removed_cells, original_board) # change num_removed_cells later

    cell_list = [] # 2D list, list of rows, then list of cell classes
    for row_num, row in enumerate(board):
      temp_list = []
      for col_num, number in enumerate(row):
        temp_list.append(Cell(number, row_num, col_num, screen))

      cell_list.append(temp_list)

    draw_game_screen(screen, sudoku_board)

    for event in pygame.event.get():
      if event.type == pygame.QUIT: # Quitting out
        pygame.quit()


    if sudoku_board.is_full(cell_list) and sudoku_board.check_board(): # Player has won the game
      draw_end_screen(screen)

    for row in cell_list:
      for cell in row:
        cell.draw()
    
    pygame.display.update() # Updating display

      