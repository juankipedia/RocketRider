from typing import Any, Dict, Tuple

import pygame
from pygame.locals import *

from .BaseState import BaseState

import settings

from src.space_object import SpaceObject
from src.spacecraft import Spacecraft
from src.enemy import Enemy
from src.projectile import Projectile

from src.camera import get_camera_position

class PlayState(BaseState):
    def enter(self, **params: Dict[str, Any]) -> None:
        self.spacecraft = Spacecraft(settings.WORLD_WIDTH // 2, settings.WORLD_HEIGHT // 2)
        self.enemy_projectiles = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.enemy = Enemy(settings.WORLD_WIDTH // 2, settings.WORLD_HEIGHT // 2, self.spacecraft, self.enemy_projectiles, self.all_sprites)
        self.player_projectiles = pygame.sprite.Group()
        self.all_sprites.add(self.spacecraft)
        self.all_sprites.add(self.enemy)
        self.camera_x, self.camera_y = 0, 0

    def exit(self) -> None:
        pass

    def update(self, dt: float) -> None:
        
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[K_SPACE] and self.spacecraft.alive():
            proj = Projectile(self.spacecraft.rect.centerx, self.spacecraft.rect.centery, self.spacecraft.angle, speed=100)
            self.player_projectiles.add(proj)
            self.all_sprites.add(proj)

        self.all_sprites.update(keys_pressed, dt)
        self.camera_x, self.camera_y = get_camera_position(self.spacecraft, settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT, settings.WORLD_WIDTH, settings.WORLD_HEIGHT, self.camera_x, self.camera_y)

        for proj in self.enemy_projectiles:
            if self.spacecraft.rect.colliderect(proj.rect):
                proj.kill()
                self.spacecraft.take_damage(2)
                if self.spacecraft.hp <= 0:
                    self.spacecraft.kill()

        for proj in self.player_projectiles:
            if self.enemy.rect.colliderect(proj.rect):
                proj.kill()
                self.enemy.take_damage(2)
                if self.enemy.hp <= 0:
                    self.enemy.kill()

    def render(self, surface: pygame.Surface) -> None:
        surface.blit(settings.TEXTURES["background"], (self.camera_x, self.camera_y))

        for sprite in self.all_sprites:
            surface.blit(sprite.image, sprite.rect.move(self.camera_x, self.camera_y))
            if isinstance(sprite, SpaceObject):
                sprite.draw_health_bar(surface, self.camera_x, self.camera_y)