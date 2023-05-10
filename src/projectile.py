import math
import pygame

import settings


class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, angle, speed=10, color=(255, 255, 255)):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.inflate_ip(-1, -1)
        self.rect.x = x
        self.rect.y = y
        self.angle = angle
        self.speed = speed

    def update(self, dt: float):
        dx = self.speed * math.cos(math.radians(self.angle))
        dy = self.speed * math.sin(math.radians(self.angle))
        self.rect.x = self.rect.x + dx * dt
        self.rect.y = self.rect.y - dy * dt

        if (
            self.rect.x < 0
            or self.rect.x >= settings.WORLD_WIDTH
            or self.rect.y < 0
            or self.rect.y >= settings.WORLD_HEIGHT
        ):
            self.kill()
