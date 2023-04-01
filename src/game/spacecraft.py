import pygame
from pygame.locals import *


class Spacecraft(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.original_image = pygame.image.load('../resources/spacecraft.png').convert()
        width, height = self.original_image.get_size()
        self.original_image = pygame.transform.scale(self.original_image, (width // 4, height // 4))
        self.original_image = self.original_image.convert_alpha()
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.x = screen_width // 2
        self.rect.y = screen_height // 2
        self.speed = 5
        self.angle = 0
        self.screen_width = screen_width
        self.screen_height = screen_height

    def rotate(self, angle):
        self.angle += angle
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self, keys_pressed):
        if keys_pressed[K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.bottom < self.screen_height:
            self.rect.y += self.speed
        if keys_pressed[K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.right < self.screen_width:
            self.rect.x += self.speed

        if keys_pressed[K_a]:
            self.rotate(5)
        if keys_pressed[K_d]:
            self.rotate(-5)
