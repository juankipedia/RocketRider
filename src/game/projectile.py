import math
import pygame


class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, angle, speed=10):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.angle = angle
        self.speed = speed

    def update(self, key_pressed, world_width, world_height):
        dx = self.speed * math.cos(math.radians(self.angle))
        dy = self.speed * math.sin(math.radians(self.angle))
        self.rect.x += dx
        self.rect.y -= dy

        if self.rect.x < 0 or self.rect.x > world_width or self.rect.y < 0 or self.rect.y > world_height:
            self.kill()
