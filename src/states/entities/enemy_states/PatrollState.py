import random

import settings

from src.states.entities.BaseEntityState import BaseEntityState

class PatrollState(BaseEntityState):
    def enter(self, flipped: bool) -> None:
        self.entity.change_animation("walk")
        self.entity.move_direction = 'stay'
        self.entity.move_counter = 0
        self.entity.vx = self.entity.vy = 0

    def update(self, dt: float) -> None:
        if self.entity.move_counter == 0:

            self.entity.move_direction = random.choice(['up', 'down', 'left', 'right', 'stay'])
            self.entity.move_counter = random.randint(50, 100)

            if self.entity.move_direction == 'up':
                self.entity.vy = -self.entity.walk_speed
            elif self.entity.move_direction == 'down':
                self.entity.vy = self.entity.walk_speed
            elif self.entity.move_direction == 'left':
                self.entity.vx = -self.entity.walk_speed
            elif self.entity.move_direction == 'right':
                self.entity.vx = self.entity.walk_speed
        
        if self.__check_boundaries():
            self.entity.vx *= -1
            self.entity.vy *= -1
        
        self.entity.move_counter -= 1

    def __check_boundaries(self):
        if self.entity.x + self.entity.width >= settings.WORLD_WIDTH or self.entity.x + self.entity.width >= settings.WORLD_HEIGHT:
            return True
        elif self.entity.x <= 0 or self.entity.y <= 0:
            return True
        
        return False