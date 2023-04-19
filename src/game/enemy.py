import random
from pygame.locals import *
from space_object import SpaceObject
from projectile import *

class Enemy(SpaceObject):
    def __init__(self, screen_width, screen_height):
        super().__init__('../resources/enemy.png', screen_width, screen_height)
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = random.randint(0, screen_height - self.rect.height)
        self.move_counter = 0
        self.move_direction = 'STAY'
        self.rotation_counter = 0
        self.target_angle = 0
        self.shoot_timer = random.randint(30, 120)
        self.max_hp = 50
        self.hp = self.max_hp
        self.acceleration = 0.05
        self.drag_coefficient = 0.98

    def update(self, keys_pressed, world_width, world_height):
        if self.move_counter <= 0:
            self.move_direction = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT', 'STAY'])
            self.move_counter = random.randint(50, 100)

        if self.move_direction == 'UP':
            self.velocity_y -= self.acceleration
        elif self.move_direction == 'DOWN':
            self.velocity_y += self.acceleration
        elif self.move_direction == 'LEFT':
            self.velocity_x -= self.acceleration
        elif self.move_direction == 'RIGHT':
            self.velocity_x += self.acceleration

        if self.rotation_counter <= 0:
            self.rotation_counter = random.randint(30, 120)
            self.target_angle = random.randint(-90, 90)

        angle_diff = self.target_angle - self.angle
        angle_change = angle_diff * 0.05
        self.rotate(angle_change)

        self.move_counter -= 1
        self.shoot_timer -= 1

        super().update(keys_pressed, world_width, world_height)

    def shoot(self, n_projectiles=10, angle_range=30):
        base_angle = self.angle - angle_range / 2
        angle_step = angle_range / (n_projectiles - 1)
        projectiles = []
        for i in range(n_projectiles):
            angle = base_angle + angle_step * i
            proj = Projectile(self.rect.centerx, self.rect.centery, angle, color=(255, 0, 0))
            projectiles.append(proj)
        return projectiles
