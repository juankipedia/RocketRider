import sys
import os
import pygame
import json
from pygame.locals import *
from spacecraft import *
from enemy import *
from projectile import *
from config import SCREEN_WIDTH, SCREEN_HEIGHT, WORLD_WIDTH, WORLD_HEIGHT
from camera import get_camera_position

pygame.init()

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('RocketRider')
    spacecraft = Spacecraft(WORLD_WIDTH // 2, WORLD_HEIGHT // 2)
    enemy = Enemy(WORLD_WIDTH // 2, WORLD_HEIGHT // 2)
    all_sprites = pygame.sprite.Group()
    player_projectiles = pygame.sprite.Group()
    enemy_projectiles = pygame.sprite.Group()
    enemy_projectiles = set()
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

        if keys_pressed[K_SPACE] and spacecraft.alive():
            proj = Projectile(spacecraft.rect.centerx, spacecraft.rect.centery, spacecraft.angle)
            player_projectiles.add(proj)
            all_sprites.add(proj)
        
        if enemy.shoot_timer <= 0:
            enemy_projectiles_list = enemy.shoot()
            for proj in enemy_projectiles_list:
                enemy_projectiles.add(proj)
                all_sprites.add(proj)
            enemy.shoot_timer = random.randint(30, 120)

        all_sprites.update(keys_pressed, WORLD_WIDTH, WORLD_HEIGHT)
        camera_x, camera_y = get_camera_position(spacecraft, SCREEN_WIDTH, SCREEN_HEIGHT, WORLD_WIDTH, WORLD_HEIGHT, camera_x, camera_y)

        screen.blit(background_image, (camera_x, camera_y))
        
        for proj in enemy_projectiles:
            if spacecraft.rect.colliderect(proj.rect):
                proj.kill()
                spacecraft.take_damage(2)
                if spacecraft.hp <= 0:
                    spacecraft.kill()

        for proj in player_projectiles:
            if enemy.rect.colliderect(proj.rect):
                proj.kill()
                enemy.take_damage(2)
                if enemy.hp <= 0:
                    enemy.kill()

        for sprite in all_sprites:
            screen.blit(sprite.image, sprite.rect.move(camera_x, camera_y))
            if isinstance(sprite, SpaceObject):
                sprite.draw_health_bar(screen, camera_x, camera_y)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
