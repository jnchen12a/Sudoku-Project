import pygame
from constants import *
from board import Board
from cell import Cell
from sudoku_generator import SudokuGenerator
from sudoku_generator import generate_sudoku
import sys

def get_cord(pos):
  x = pos[0] // SQUARE_SIZE
  y = pos[1] // SQUARE_SIZE
  return x, y

def draw_start_screen(screen): # Return number of removed cells
  screen.fill(WHITE)
  button_font = pygame.font.Font(None, 65)
  select_game_mode_font = pygame.font.Font(None, 55)
  game_mode_font = pygame.font.Font(None, 35)
  title_surf = button_font.render('Welcome to Sudoku!', 0, BLACK)
  title_rect = title_surf.get_rect(center=(WIDTH // 2, (SCREEN_LENGTH // 2) - 150))
  screen.blit(title_surf, title_rect)

  # Create select game mode text
  select_game_mode = select_game_mode_font.render('Select Game Mode:', 0, BLACK)
  select_game_mode_rect = select_game_mode.get_rect(center=(WIDTH // 2, (SCREEN_LENGTH // 2) - 25))
  screen.blit(select_game_mode, select_game_mode_rect)
  
  # Initialize 'Easy' Button and Text
  easy_text = game_mode_font.render("EASY", 0, BLACK)

  # Initialize 'Easy' Button Background Color and Text
  easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
  easy_surface.fill(RED)
  easy_surface.blit(easy_text, (10, 10))

  # Initialize 'Easy' Button Rectangle
  easy_rectangle = easy_surface.get_rect(center=(WIDTH // 4, SCREEN_LENGTH // 2 + 50))

  # Draws 'Easy' Buttons
  screen.blit(easy_surface, easy_rectangle)

  # Initialize 'Medium' Button and Text
  medium_text = game_mode_font.render("MEDIUM", 0, BLACK)

  # Initialize 'Medium' Button Background Color and Text
  medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
  medium_surface.fill(RED)
  medium_surface.blit(medium_text, (10, 10))

  # Initialize 'Medium' Button Rectangle
  medium_rectangle = medium_surface.get_rect(center=((WIDTH // 4) * 2, SCREEN_LENGTH // 2 + 50))

  # Draws 'Medium' Buttons
  screen.blit(medium_surface, medium_rectangle)

    # Initialize 'Hard' Button and Text
  hard_text = game_mode_font.render("HARD", 0, BLACK)

  # Initialize 'Hard' Button Background Color and Text
  hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
  hard_surface.fill(RED)
  hard_surface.blit(hard_text, (10, 10))

  # Initialize 'Hard' Button Rectangle
  hard_rectangle = hard_surface.get_rect(center=((WIDTH // 4) * 3, SCREEN_LENGTH // 2 + 50))

  # Draws 'Hard' Buttons
  screen.blit(hard_surface, hard_rectangle)
  
  while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
          if easy_rectangle.collidepoint(event.pos):
            return 30
          if medium_rectangle.collidepoint(event.pos):
            return 40
          if hard_rectangle.collidepoint(event.pos):
            return 50

    pygame.display.update()

def draw_game_screen(screen, board):
  x = None
  y = None
  # Use draw() method from Board class

  # Initialize fonts
  font = pygame.font.Font(None, 30)

  #Background Color


  while True:
    used = False
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if reset_rectangle.collidepoint(event.pos):
          sudoku_board.reset_to_original(cell_list)
        if restart_rectangle.collidepoint(event.pos):
          return 'restart'
        if exit_rectangle.collidepoint(event.pos):
          pygame.quit()
        if finish_rectangle.collidepoint(event.pos):
          return 'finish'
        pos = pygame.mouse.get_pos()
        x, y = get_cord(pos)
      if event.type == pygame.KEYDOWN:
        if x == None or y == None:
          used = True
        default_cell_y, default_cell_x = (removed_cells[0] // 9), (removed_cells[0] % 9)
        x = default_cell_x if x == None else x
        y = default_cell_y if y == None else y
        id = (y * 9) + x
        if event.key == pygame.K_1:
          if id in removed_cells:
            cell_list[int(y)][int(x)].set_sketched_value(1)
        if event.key == pygame.K_2:
          if id in removed_cells:
            cell_list[int(y)][int(x)].set_sketched_value(2)
        if event.key == pygame.K_3:
          if id in removed_cells:
            cell_list[int(y)][int(x)].set_sketched_value(3)
        if event.key == pygame.K_4:
          if id in removed_cells:
            cell_list[int(y)][int(x)].set_sketched_value(4)
        if event.key == pygame.K_5:
          if id in removed_cells:
            cell_list[int(y)][int(x)].set_sketched_value(5)
        if event.key == pygame.K_6:
          if id in removed_cells:
            cell_list[int(y)][int(x)].set_sketched_value(6)
        if event.key == pygame.K_7:
          if id in removed_cells:
            cell_list[int(y)][int(x)].set_sketched_value(7)
        if event.key == pygame.K_8:
          if id in removed_cells:
            cell_list[int(y)][int(x)].set_sketched_value(8)
        if event.key == pygame.K_9:
          if id in removed_cells:
            cell_list[int(y)][int(x)].set_sketched_value(9)
        if event.key == pygame.K_RETURN:
          if id in removed_cells:
            cell_list[int(y)][int(x)].set_cell_value(cell_list[int(y)][int(x)].sketched_value)
            cell_list[int(y)][int(x)].set_sketched_value(0)
        if event.key == pygame.K_UP:
          if not used:
            y = y - 1 if y != 0 else 0
        if event.key == pygame.K_DOWN:
          if not used:
            y = y + 1 if y != 8 else 8
        if event.key == pygame.K_RIGHT:
          if not used:
            x = x + 1 if x != 8 else 8
        if event.key == pygame.K_LEFT:
          if not used:
            x = x - 1 if x != 0 else 0

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
    sudoku_board.select(y, x, removed_cells)
    for row_num, row in enumerate(cell_list):
      for col, cell in enumerate(row):
        cell.sketch_sketched_num(row_num, col, screen)
        cell.sketch_num(row_num, col, screen)
    
    pygame.display.update()
    
    if sudoku_board.is_full(cell_list):
      pygame.time.wait(1500)
      return 'finish'

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
  
  while True: # Game loop
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
    choice = draw_game_screen(screen, sudoku_board)

    if choice == 'restart':
      continue
    elif choice == 'finish':
      if sudoku_board.is_full(cell_list):
        if sudoku_board.check_board(cell_list):
          draw_win_screen(screen)
        else:
          draw_lost_screen(screen)
      else:
        draw_lost_screen(screen)

      