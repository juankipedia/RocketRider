import random
from pygame.locals import *
from space_object import SpaceObject


class Enemy(SpaceObject):
    def __init__(self, screen_width, screen_height):
        super().__init__('../resources/enemy.png', screen_width, screen_height)
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = random.randint(0, screen_height - self.rect.height)
        self.move_counter = 0
        self.move_direction = 'STAY'
        self.rotation_counter = 0
        self.target_angle = 0

    def update(self, keys_pressed, world_width, world_height):
        if self.move_counter <= 0:
            self.move_direction = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT', 'STAY'])
            self.move_counter = random.randint(50, 100)

        if self.move_direction == 'UP' and self.rect.top > 0:
            self.rect.y -= self.speed
        elif self.move_direction == 'DOWN' and self.rect.bottom < world_height:
            self.rect.y += self.speed
        elif self.move_direction == 'LEFT' and self.rect.left > 0:
            self.rect.x -= self.speed
        elif self.move_direction == 'RIGHT' and self.rect.right < world_width:
            self.rect.x += self.speed

        if self.rotation_counter <= 0:
            self.rotation_counter = random.randint(30, 120)
            self.target_angle = random.randint(-90, 90)

        angle_diff = self.target_angle - self.angle
        angle_change = angle_diff * 0.05
        self.rotate(angle_change)

        self.move_counter -= 1

        super().update(keys_pressed, world_width, world_height)

