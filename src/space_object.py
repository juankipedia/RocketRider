import pygame
from pygame.locals import *

import settings

class SpaceObject(pygame.sprite.Sprite):
    def __init__(self, image_name, screen_width, screen_height):
        super().__init__()
        self.original_image = settings.TEXTURES[image_name].convert()
        width, height = self.original_image.get_size()
        self.image_scale_ratio = 3
        self.original_image = pygame.transform.scale(self.original_image, 
                                                     (width // self.image_scale_ratio, height // self.image_scale_ratio))
        self.original_image = self.original_image.convert_alpha()
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.inflate_ip(-5, -5)
        self.rect.x = screen_width // 2
        self.rect.y = screen_height // 2
        self.speed = 1
        self.angle = 0
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.acceleration = 0
        self.velocity_x = 0
        self.velocity_y = 0
        self.drag_coefficient = 1

    def rotate(self, angle):
        self.angle += angle
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)


    def update(self, keys_pressed, dt: float):
        self.velocity_x *= self.drag_coefficient
        self.velocity_y *= self.drag_coefficient

        self.rect.x = self.rect.x + self.velocity_x * dt
        self.rect.y = self.rect.y + self.velocity_y * dt

        self.rect.x = max(0, min(settings.WORLD_WIDTH - self.rect.width, self.rect.x))
        self.rect.y = max(0, min(settings.WORLD_HEIGHT - self.rect.height, self.rect.y))

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.kill()

    def draw_health_bar(self, screen, camera_x, camera_y):
        hp_bar_width = self.rect.width
        hp_bar_height = 5
        hp_bar_color = (255, 0, 0)
        hp_bar_bg_color = (128, 128, 128)

        hp_ratio = self.hp / self.max_hp
        hp_width = int(hp_ratio * hp_bar_width)

        hp_bar_rect = pygame.Rect(0, 0, hp_bar_width, hp_bar_height)
        hp_bar_rect.x = self.rect.x
        hp_bar_rect.y = self.rect.y - hp_bar_height - 2
        hp_bar_rect.move_ip(camera_x, camera_y)
        screen.fill(hp_bar_bg_color, hp_bar_rect)

        hp_rect = pygame.Rect(0, 0, hp_width, hp_bar_height)
        hp_rect.x = self.rect.x
        hp_rect.y = self.rect.y - hp_bar_height - 2
        hp_rect.move_ip(camera_x, camera_y)
        screen.fill(hp_bar_color, hp_rect)