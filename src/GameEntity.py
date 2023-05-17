from typing import TypeVar, Dict, Any, Tuple

import settings

from src.mixins import AnimatedMixin, CollidableMixin, DrawableMixin
from src.states.BaseState import BaseState
from src.states.StateMachine import StateMachine

class GameEntity(AnimatedMixin, CollidableMixin, DrawableMixin):
    def __init__(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
        texture_id: str,
        game_level: TypeVar("GameLevel"),
        states: Dict[str, BaseState],
        animation_defs: Dict[str, Dict[str, Any]],
    ) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vx: float = 0
        self.vy: float = 0
        self.texture_id = texture_id
        self.frame_index = -1
        self.game_level = game_level
        # self.tilemap = self.game_level.tilemap
        self.state_machine = StateMachine(states)
        self.current_animation = None
        self.animations = {}
        self.generate_animations(animation_defs)
        self.flipped = False
        self.is_dead = False

    def change_state(
        self, state_id: str, *args: Tuple[Any], **kwargs: Dict[str, Any]
    ) -> None:
        self.state_machine.change(state_id, *args, **kwargs)

    def update(self, dt: float) -> None:
        self.state_machine.update(dt)
        AnimatedMixin.update(self, dt)

        self.x = self.x + self.vx * dt
        self.y = self.y + self.vy * dt

        self.x = max(0, min(settings.WORLD_WIDTH - self.width, self.x))
        self.y = max(0, min(settings.WORLD_HEIGHT - self.height, self.y))
