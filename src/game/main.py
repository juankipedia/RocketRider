import sys
import pygame
from pygame.locals import *
from spacecraft import *

pygame.init()


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('RocketRider')


BLACK = (0, 0, 0)
LIGHT_BLUE = (173, 216, 230)


spacecraft = Spacecraft(screen_width, screen_height)
all_sprites = pygame.sprite.Group()
all_sprites.add(spacecraft)

clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys_pressed = pygame.key.get_pressed()
    spacecraft.update(keys_pressed)

    screen.fill(LIGHT_BLUE)
    all_sprites.draw(screen)
    pygame.display.flip()

    clock.tick(60)
