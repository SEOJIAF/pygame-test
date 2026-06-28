from operator import imod
import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join

from pygame.constants import QUIT

pygame.init()

pygame.display.set_caption("Pygame Project")


BG_COLOR = (0, 0, 0)
WIDHT, HEIGHT = 800, 600

FPS = 60
PLAYER_VEL = 5

window = pygame.display.set_mode((WIDHT, HEIGHT))

def get_background(name):
    image = pygame.image.load(join("assets","Background", name))
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDHT // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = [i * width, j * height]
            tiles.append(pos)

    return tiles, image



def main(window):
    clock = pygame.time.Clock()
    background = get_background("Blue.png")

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

    pygame.quit()
    quit()


if __name__ == "__main__":
    main(window)