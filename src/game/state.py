import random
import math

class State:
    def __init__(self, enemy):
        self.enemy = enemy

    def enter(self):
        pass

    def update(self):
        pass

    def exit(self):
        pass

class PatrollingState(State):

    def enter(self):
        self.enemy.move_counter = 0
        self.enemy.move_direction = 'STAY'
        self.enemy.rotation_counter = 0
        self.enemy.target_angle = 0

    def update(self):
        if self.enemy.move_counter <= 0:
            self.enemy.move_direction = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT', 'STAY'])
            self.enemy.move_counter = random.randint(50, 100)

        if self.enemy.move_direction == 'UP' and self.enemy.rect.top > 0:
            self.enemy.rect.y -= self.enemy.speed
        elif self.enemy.move_direction == 'DOWN' and self.enemy.rect.bottom < self.enemy.screen_height:
            self.enemy.rect.y += self.enemy.speed
        elif self.enemy.move_direction == 'LEFT' and self.enemy.rect.left > 0:
            self.enemy.rect.x -= self.enemy.speed
        elif self.enemy.move_direction == 'RIGHT' and self.enemy.rect.right < self.enemy.screen_width:
            self.enemy.rect.x += self.enemy.speed

        if self.enemy.rotation_counter <= 0:
            self.enemy.rotation_counter = random.randint(30, 120)
            self.enemy.target_angle = random.randint(-90, 90)

        angle_diff = self.enemy.target_angle - self.enemy.angle
        angle_change = angle_diff * 0.05
        self.enemy.rotate(angle_change)

        self.enemy.move_counter -= 1
        self.enemy.shoot_timer -= 1


class AttackingState(State):
    def update(self):
        dx = self.enemy.target.rect.centerx - self.enemy.rect.centerx
        dy = self.enemy.target.rect.centery - self.enemy.rect.centery
        target_angle = math.degrees(math.atan2(-dy, dx))

        angle_diff = target_angle - self.enemy.angle
        angle_change = angle_diff * 0.05
        self.enemy.rotate(angle_change)

        self.enemy.shoot_timer -= 1
        if self.enemy.shoot_timer <= 0:
            self.enemy.shoot_timer = random.randint(15, 60)
            projectiles = self.enemy.shoot(n_projectiles=6, angle_range=30)
            for proj in projectiles:
                self.enemy.projectile_group.add(proj)
                self.enemy.all_sprites.add(proj)


