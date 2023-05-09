from pygame.locals import *

from src.space_object import SpaceObject

class Spacecraft(SpaceObject):
    def __init__(self, screen_width, screen_height):
        super().__init__('spacecraft', screen_width, screen_height)
        self.speed = 2
        self.max_hp = 100
        self.hp = self.max_hp
        self.acceleration = 600
        self.drag_coefficient = 0.98


    def update(self, keys_pressed, dt: float):
        if keys_pressed[K_UP]:
            self.velocity_y =  self.velocity_y - self.acceleration * dt
        if keys_pressed[K_DOWN]:
            self.velocity_y = self.velocity_y + self.acceleration * dt
        if keys_pressed[K_LEFT]:
            self.velocity_x = self.velocity_x - self.acceleration * dt
        if keys_pressed[K_RIGHT]:
            self.velocity_x = self.velocity_x + self.acceleration * dt

        if keys_pressed[K_a]:
            self.rotate(3)
        if keys_pressed[K_d]:
            self.rotate(-3)

        super().update(keys_pressed, dt)
    