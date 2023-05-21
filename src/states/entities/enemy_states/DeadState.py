from typing import Any, Dict, Tuple
from src.states.entities.BaseEntityState import BaseEntityState

class DeadState(BaseEntityState):
    def enter(self) -> None:
        self.entity.texture_id = "explosion"
        self.entity.change_animation("dead")
    
    def update(self, dt: float) -> None:
        if self.entity.frame_index == 5:
            self.entity.is_dead = True