# Basic pygame template
import pygame
from sudoku_generator import SudokuGenerator

pygame.init()
pygame.display.set_caption('Test')
screen = pygame.display.set_mode((600, 800))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()
