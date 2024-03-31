import pygame
import sys
from grid import Grid 
from blocks import *

# Define the dark_blue color using RGB values
dark_blue = (44, 44, 127)

pygame.init()

screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

game_grid = Grid()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Drawing
    screen.fill(dark_blue)
    game_grid.draw(screen)
    pygame.display.update()
    clock.tick(60)

