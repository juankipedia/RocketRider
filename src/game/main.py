import sys
import os
import pygame
import json
from pygame.locals import *
from spacecraft import *
from enemy import *
from projectile import *

with open('config.json', 'r') as file:
    config = json.load(file)

SCREEN_WIDTH = config["screen_width"]
SCREEN_HEIGHT = config["screen_height"]
WORLD_WIDTH = config["world_width"]
WORLD_HEIGHT = config["world_height"]

pygame.init()

def lerp(a, b, t):
    return a + (b - a) * t

def get_camera_position(spacecraft, SCREEN_WIDTH, SCREEN_HEIGHT, WORLD_WIDTH, WORLD_HEIGHT, camera_x, camera_y, smoothness=0.05):
    target_x = -spacecraft.rect.x + SCREEN_WIDTH // 2
    target_y = -spacecraft.rect.y + SCREEN_HEIGHT // 2

    target_x = min(0, target_x)
    target_y = min(0, target_y)
    target_x = max(-(WORLD_WIDTH - SCREEN_WIDTH), target_x)
    target_y = max(-(WORLD_HEIGHT - SCREEN_HEIGHT), target_y)

    x = lerp(camera_x, target_x, smoothness)
    y = lerp(camera_y, target_y, smoothness)

    return round(x), round(y)


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('RocketRider')
    spacecraft = Spacecraft(WORLD_WIDTH // 2, WORLD_HEIGHT // 2)
    enemy = Enemy(WORLD_WIDTH // 2, WORLD_HEIGHT // 2)
    all_sprites = pygame.sprite.Group()
    projectiles = pygame.sprite.Group()
    all_sprites.add(spacecraft)
    all_sprites.add(enemy)

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

        if keys_pressed[K_SPACE]:
            proj = Projectile(spacecraft.rect.centerx, spacecraft.rect.centery, spacecraft.angle)
            projectiles.add(proj)
            all_sprites.add(proj)
        
        if enemy.shoot_timer <= 0:
            enemy_projectiles = enemy.shoot()
            projectiles.add(*enemy_projectiles)
            all_sprites.add(*enemy_projectiles)
            enemy.shoot_timer = random.randint(30, 120)

        all_sprites.update(keys_pressed, WORLD_WIDTH, WORLD_HEIGHT)
        camera_x, camera_y = get_camera_position(spacecraft, SCREEN_WIDTH, SCREEN_HEIGHT, WORLD_WIDTH, WORLD_HEIGHT, camera_x, camera_y)

        screen.blit(background_image, (camera_x, camera_y))
        for sprite in all_sprites:
            screen.blit(sprite.image, sprite.rect.move(camera_x, camera_y))
        
        pygame.display.flip()

        clock.tick(60)

if __name__ == "__main__":
    main()
