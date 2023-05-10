from typing import TypeVar

import pygame

import settings

from src.space_object import SpaceObject
from src.projectile import Projectile


class Spacecraft(SpaceObject):
    def __init__(self, screen_width, screen_height):
        super().__init__("spacecraft", screen_width, screen_height)
        self.max_hp = 100
        self.hp = self.max_hp
        self.drag_coefficient = 0.98

    def handle_inputs(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.acceleration_y = -600
            elif event.key == pygame.K_DOWN:
                self.acceleration_y = 600
            elif event.key == pygame.K_LEFT:
                self.acceleration_x = -600
            elif event.key == pygame.K_RIGHT:
                self.acceleration_x = 600

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.acceleration_y = 0
            elif event.key == pygame.K_DOWN:
                self.acceleration_y = 0
            elif event.key == pygame.K_LEFT:
                self.acceleration_x = 0
            elif event.key == pygame.K_RIGHT:
                self.acceleration_x = 0

    def handle_pressed_inputs(self, play_state: TypeVar("PlayState")) -> None:
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_SPACE] and self.alive():
            proj = Projectile(
                self.rect.centerx,
                self.rect.centery,
                self.angle,
                speed=100,
            )
            play_state.player_projectiles.add(proj)
            play_state.all_sprites.add(proj)

        if keys_pressed[pygame.K_a]:
            self.rotate(3)
        elif keys_pressed[pygame.K_d]:
            self.rotate(-3)

    def update(self, dt: float) -> None:
        self.velocity_y = self.velocity_y + self.acceleration_y * dt
        self.velocity_x = self.velocity_x + self.acceleration_x * dt
        super().update(dt)
