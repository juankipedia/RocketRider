import pygame
from pygame.locals import *


class SpaceObject(pygame.sprite.Sprite):
    def __init__(self, image_path, screen_width, screen_height):
        super().__init__()
        self.original_image = pygame.image.load(image_path).convert()
        width, height = self.original_image.get_size()
        self.original_image = pygame.transform.scale(self.original_image, (width // 4, height // 4))
        self.original_image = self.original_image.convert_alpha()
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.x = screen_width // 2
        self.rect.y = screen_height // 2
        self.speed = 2
        self.angle = 0
        self.screen_width = screen_width
        self.screen_height = screen_height

    def rotate(self, angle):
        self.angle += angle
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)


    def update(self, keys_pressed, world_width, world_height):
        self.rect.x = max(0, min(world_width - self.rect.width, self.rect.x))
        self.rect.y = max(0, min(world_height - self.rect.height, self.rect.y))