import pygame
from constants import *

if __name__ == '__main__':
  pygame.init()
  pygame.display.set_caption('Sudoku') # Title of the window
  screen = pygame.display.set_mode((600, 600)) # Size of the display
  
  while True: # Event loop
    for event in pygame.event.get():
      if event.type == pygame.QUIT: # Quitting out
        pygame.quit()

    pygame.display.update() # Updating display