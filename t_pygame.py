# Basic pygame template
import pygame
from sudoku_generator import SudokuGenerator
from constants import *
from board import Board

pygame.init()
pygame.display.set_caption('Test')
screen = pygame.display.set_mode((LENGTH, WIDTH))
screen.fill((255, 255, 245)) # Makes screen white, in rgb, https://www.google.com/search?q=rgb+color+picker&oq=rgb+&aqs=chrome.1.69i57j0i67i131i433j0i67l2j0i67i433l2j0i67j0i67i433l2j0i67.3976j0j7&sourceid=chrome&ie=UTF-8

board = Board(WIDTH, LENGTH, screen, 1)
board.draw()
board.select(2, 2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()
