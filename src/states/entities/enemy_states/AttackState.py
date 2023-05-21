import math

import settings

from src.states.entities.BaseEntityState import BaseEntityState
from src.Projectile import Projectile
from src.definitions import projectiles


class AttackState(BaseEntityState):
    def enter(self) -> None:
        self.entity.change_animation("idle")
        self.shoot()
        self.entity.change_state("patroll")

    def shoot(self) -> None:
        # settings.SOUNDS["laser_shoot2"].play()

        # Calculate direction towards the player
        dx = self.entity.game_level.player.x - self.entity.x
        dy = self.entity.game_level.player.y - self.entity.y

        # Normalize the direction vector
        distance = math.sqrt(dx**2 + dy**2)
        if distance != 0:
            dx /= distance
            dy /= distance

        definition = projectiles.PROJECTILES[self.entity.projectile_id]
        definition.update(
            x=self.entity.x,
            y=self.entity.y,
            width=settings.ENEMY_PROYECTILE_WIDTH,
            height=settings.ENEMY_PROYECTILE_HEIGHT,
            vx=dx*self.entity.projectile_speed,
            vy=dy*self.entity.projectile_speed,
        )
        
        self.entity.game_level.projectiles.append(Projectile(**definition))
