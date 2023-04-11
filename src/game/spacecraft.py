from pygame.locals import *
from space_object import SpaceObject

class Spacecraft(SpaceObject):
    def __init__(self, screen_width, screen_height):
        super().__init__('../resources/spacecraft.png', screen_width, screen_height)
        self.speed = 5
        self.max_hp = 100
        self.hp = self.max_hp

    def update(self, keys_pressed, world_width, world_height):
        if keys_pressed[K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.bottom < world_height:
            self.rect.y += self.speed
        if keys_pressed[K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.right < world_width:
            self.rect.x += self.speed

        if keys_pressed[K_a]:
            self.rotate(5)
        if keys_pressed[K_d]:
            self.rotate(-5)

        super().update(keys_pressed, world_width, world_height)
