import random
import math

from typing import Any, Dict, Tuple

import settings

from src.states.entities.BaseEntityState import BaseEntityState


class ChaseState(BaseEntityState):
    def enter(self) -> None:
        self.entity.change_animation("walk")
        self.entity.move_direction = random.choice(['left', 'right'])
        
        if self.entity.move_direction == 'left':
            self.entity.vx = random.randint(-self.entity.walk_speed, 1)
        elif self.entity.move_direction == 'right':
            self.entity.vx = random.randint(1, self.entity.walk_speed)

        self.entity.vy = random.randint(1, self.entity.walk_speed)

    def update(self, dt: float) -> None:
        # Calculate direction towards the player
        # dx = self.entity.game_level.player.x - self.entity.x
        # dy = self.entity.game_level.player.y - self.entity.y

        # Normalize the direction vector
        # distance = math.sqrt(dx**2 + dy**2)
        # if distance != 0:
        #     dx /= distance
        #     dy /= distance

        if self.__check_boundaries():
            self.entity.vx *= -1

    def __check_boundaries(self):
        if self.entity.x + self.entity.width >= settings.WORLD_WIDTH or self.entity.x <= 0:
            return True
        
        return False
