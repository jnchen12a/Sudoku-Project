import pygame
from constants import *
from board import Board
from cell import Cell
from sudoku_generator import SudokuGenerator

def draw_start_screen(screen):
  screen.fill(WHITE)
  font = pygame.font.Font(None, 40)
  title_surf = font.render('Sudoku!', 0, BLACK)
  title_rect = title_surf.get_rect(center=(WIDTH // 2, (LENGTH // 2) - 150))
  screen.blit(title_surf, title_rect)

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()

def draw_difficulty_screen(screen):
  pass

def draw_game_screen(screen):
  pass

def draw_end_screen(screen):
  pass

if __name__ == '__main__':
  pygame.init()
  pygame.display.set_caption('Sudoku') # Title of the window
  screen = pygame.display.set_mode((WIDTH, LENGTH)) # Size of the display
  # screen.fill(WHITE)

  print('Hello')
  draw_start_screen(screen)
  print('world')
  
  while True: # Event loop
    for event in pygame.event.get():
      if event.type == pygame.QUIT: # Quitting out
        pygame.quit()

    pygame.display.update() # Updating display