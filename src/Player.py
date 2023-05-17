from typing import Any, Dict, TypeVar

import pygame

import settings

from src.GameEntity import GameEntity
from src.states.entities.player_states import IdleState, MoveState
from src.Boosters import Boosters


class Player(GameEntity):
    def __init__(self, x: float, y: float, game_level: TypeVar("GameLevel")) -> None:
        super().__init__(
            x,
            y,
            settings.SPACESHIP_WIDTH,
            settings.SPACESHIP_HEIGHT,
            "spaceship",
            game_level,
            states={
                "idle": lambda sm: IdleState(self, sm),
                "move": lambda sm: MoveState(self, sm),
            },
            animation_defs={
                "idle": {"frames": [1]},
                "move_left": {"frames": [0]},
                "move_right": {"frames": [2]},
            },
        )
        self.max_hp = settings.SPACESHIP_HP
        self.hp = self.max_hp
        self.boosters = Boosters(
            x + settings.BOOSTERS_OFFSET_X,
            y + settings.BOOSTERS_OFFSET_Y,
            settings.BOOSTERS_WIDTH,
            settings.BOOSTERS_HEIGHT,
            "boosters",
            animation_defs={"power_on": {"frames": [0, 1], "interval": 0.075}},
        )
        self.boosters.change_animation("power_on")

    def handle_inputs(self, event: pygame.event.Event):
        self.state_machine.handle_inputs(event)

    def update(self, dt: float) -> None:
        super().update(dt)
        self.boosters.x = self.x + settings.BOOSTERS_OFFSET_X
        self.boosters.y = self.y + settings.BOOSTERS_OFFSET_Y
        self.boosters.update(dt)

    def render(self, surface: pygame.Surface) -> None:
        super().render(surface)
        self.boosters.render(surface)
