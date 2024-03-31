import pygame
import sys
from game import Game

# Define the dark_blue color using RGB values
dark_blue = (44, 44, 127)

pygame.init()

screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

game = Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
    # Drawing
    screen.fill(dark_blue)
    game.draw(screen)

    pygame.display.update()
    clock.tick(60)

