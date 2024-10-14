from turtledemo.nim import SCREENWIDTH, SCREENHEIGHT

import pygame
import random
from Tools.scripts.dutree import display
from pygame.examples.cursors import image
from pygame.examples.go_over_there import running

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
pygame.display.set_caption("Тир")
icon = pygame.image.load("image/tir.gif")
pygame.display.set_icon(icon)

target_image = pygame.image.load("image/strelok.png")
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT- target_height)

color = (random.randint(0,255), random.randint(0,255),random.randint(0,255))

running = True
while running:
    pass

pygame.quit()