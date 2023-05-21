import settings

from src.states.entities.BaseEntityState import BaseEntityState

from src.Projectile import Projectile
from src.definitions import projectiles

class AttackState(BaseEntityState):
    def enter(self) -> None:
        settings.SOUNDS["laser_shoot"].play()
        definition = projectiles.PROJECTILES["player_charged_beam"]
        definition.update(
            x=self.entity.x,
            y=self.entity.y,
            width=settings.SPACESHIP_PROYECTILE_WIDTH,
            height=settings.SPACESHIP_PROYECTILE_HEIGHT,
            vx=0,
            vy=-settings.SPACESHIP_PROYECTILE_SPEED,
        )
        self.entity.projectiles.append(Projectile(**definition))
        self.entity.change_state("idle")

    def update(self, dt: float) -> None:
        pass