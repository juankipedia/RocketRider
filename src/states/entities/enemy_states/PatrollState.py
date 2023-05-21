import math
import random

import settings

from src.states.entities.BaseEntityState import BaseEntityState

class PatrollState(BaseEntityState):
    def enter(self) -> None:
        self.entity.change_animation("walk")
        self.entity.move_direction = random.choice(['left', 'right'])
        
        if self.entity.move_direction == 'left':
            self.entity.vx = random.randint(-self.entity.walk_speed, 1)
        elif self.entity.move_direction == 'right':
            self.entity.vx = random.randint(1, self.entity.walk_speed)
        
        self.entity.vy = random.randint(1, self.entity.walk_speed)

        self.shoot_time = random.randint(1, 3)
        self.timer = 0.0

    def update(self, dt: float) -> None:
        self.timer += dt
        if self.timer >= self.shoot_time:
            self.timer = 0.0
            self.entity.change_state("attack")

        if self.__check_boundaries():
            self.entity.vx *= -1

    def __check_boundaries(self):
        if self.entity.x + self.entity.width >= settings.WORLD_WIDTH or self.entity.x <= 0:
            return True
        
        return False