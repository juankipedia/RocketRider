import random

import settings

from src.space_object import SpaceObject
from src.projectile import *
from src.state import PatrollingState, AttackingState

class Enemy(SpaceObject):
    def __init__(self, screen_width, screen_height, player, enemy_projectiles, all_sprites):
        super().__init__('enemy', screen_width, screen_height)
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = random.randint(0, screen_height - self.rect.height)
        self.move_counter = 0
        self.move_direction = 'STAY'
        self.rotation_counter = 0
        self.target_angle = 0
        self.shoot_timer = random.randint(30, 120)
        self.max_hp = settings.ENEMY_HP
        self.hp = self.max_hp
        self.acceleration = settings.ENEMY_ACCELERATION
        self.drag_coefficient = settings.ENEMY_DRAG_COEFFICIENT
        self.state = PatrollingState(self)
        self.state.enter()
        self.attack_range = settings.ENEMY_ATTACK_RANGE
        self.target = player
        self.projectile_group = enemy_projectiles
        self.all_sprites = all_sprites 

    def get_distance_to_object(self, other_object):
        dx = self.rect.centerx - other_object.rect.centerx
        dy = self.rect.centery - other_object.rect.centery
        return (dx ** 2 + dy ** 2) ** 0.5

    def update(self, dt: float):
        distance_to_player = self.get_distance_to_object(self.target)
        if distance_to_player < self.attack_range and not isinstance(self.state, AttackingState):
            self.state.exit()
            self.state = AttackingState(self)
            self.state.enter()
        elif distance_to_player >= self.attack_range and not isinstance(self.state, PatrollingState):
            self.state.exit()
            self.state = PatrollingState(self)
            self.state.enter()

        self.state.update(dt)
        super().update(dt)


    def shoot(self, n_projectiles=10, angle_range=30):
        base_angle = self.angle - angle_range / 2
        angle_step = angle_range / (n_projectiles - 1)
        projectiles = []
        for i in range(n_projectiles):
            angle = base_angle + angle_step * i
            proj = Projectile(self.rect.centerx, self.rect.centery, angle, speed=settings.ENEMY_PROYECTILE_SPEED, color=(255, 0, 0))
            projectiles.append(proj)
        return projectiles
