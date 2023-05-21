import pygame

from src.states.entities.BaseEntityState import BaseEntityState

class DeadState(BaseEntityState):
    def enter(self) -> None:
        self.entity.texture_id = "sparkle"
        self.entity.change_animation("dead")
        self.entity.render_boosters = False

    def update(self, dt: float) -> None:
        if self.entity.frame_index == 4:
            self.entity.is_dead = True