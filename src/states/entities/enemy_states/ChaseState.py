import random
import math

from typing import Any, Dict, Tuple

import settings

from src.states.entities.BaseEntityState import BaseEntityState


class ChaseState(BaseEntityState):
    def enter(self, flipped: bool) -> None:
        print('enter chase')
        self.entity.change_animation("walk")
        self.entity.vx = self.entity.vy = 0

    def update(self, dt: float) -> None:
        # Calculate direction towards the player
        dx = self.entity.player.x - self.entity.x
        dy = self.entity.player.y - self.entity.y

        # Normalize the direction vector
        distance = math.sqrt(dx**2 + dy**2)
        if distance != 0:
            dx /= distance
            dy /= distance

        # Update enemy's velocity based on the direction
        speed = self.entity.walk_speed
        self.entity.vx = dx * speed
        self.entity.vy = dy * speed
