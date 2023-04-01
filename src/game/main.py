import sys
import os
import pygame
from pygame.locals import *
from spacecraft import *

pygame.init()

# Config
screen_width = 800
screen_height = 600
world_width = 1920
world_height = 1080

def lerp(a, b, t):
    return a + (b - a) * t

def get_camera_position(spacecraft, screen_width, screen_height, world_width, world_height, camera_x, camera_y, smoothness=0.05):
    target_x = -spacecraft.rect.x + screen_width // 2
    target_y = -spacecraft.rect.y + screen_height // 2

    target_x = min(0, target_x)
    target_y = min(0, target_y)
    target_x = max(-(world_width - screen_width), target_x)
    target_y = max(-(world_height - screen_height), target_y)

    x = lerp(camera_x, target_x, smoothness)
    y = lerp(camera_y, target_y, smoothness)

    return round(x), round(y)

def main():
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('RocketRider')
    spacecraft = Spacecraft(world_width // 2, world_height // 2)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(spacecraft)

    image_path = os.path.join(os.path.dirname(__file__), '..', 'resources', 'world.jpg')
    background_image = pygame.image.load(image_path).convert()

    clock = pygame.time.Clock()

    camera_x, camera_y = 0, 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        keys_pressed = pygame.key.get_pressed()
        all_sprites.update(keys_pressed, world_width, world_height)
        camera_x, camera_y = get_camera_position(spacecraft, screen_width, screen_height, world_width, world_height, camera_x, camera_y)

        screen.blit(background_image, (camera_x, camera_y))  # Dibuja la imagen de fondo
        for sprite in all_sprites:
            screen.blit(sprite.image, sprite.rect.move(camera_x, camera_y))
        
        pygame.display.flip()

        clock.tick(60)

if __name__ == "__main__":
    main()
