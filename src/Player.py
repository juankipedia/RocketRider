from typing import Any, Dict, TypeVar

import pygame

import settings

from src.GameEntity import GameEntity
from src.states.entities import player_states
from src.Boosters import Boosters


class Player(GameEntity):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(
            x,
            y,
            settings.SPACESHIP_WIDTH,
            settings.SPACESHIP_HEIGHT,
            "spaceship",
            game_level=None,
            states={
                "idle": lambda sm: player_states.IdleState(self, sm),
                "move": lambda sm: player_states.MoveState(self, sm),
                "dead": lambda sm: player_states.DeadState(self, sm),
                "attack": lambda sm: player_states.AttackState(self, sm)
            },
            animation_defs={
                "idle": {"frames": [1]},
                "move_left": {"frames": [0]},
                "move_right": {"frames": [2]},
                "dead": {"frames": [0, 1, 2, 3, 4], "interval": 0.1}
            },
        )
        self.max_hp = settings.SPACESHIP_HP
        self.hp = self.max_hp
        self.angle = 0
        self.boosters = Boosters(
            x + settings.BOOSTERS_OFFSET_X,
            y + settings.BOOSTERS_OFFSET_Y,
            settings.BOOSTERS_WIDTH,
            settings.BOOSTERS_HEIGHT,
            "boosters",
            animation_defs={"power_on": {"frames": [0, 1], "interval": 0.075}},
        )
        self.boosters.change_animation("power_on")
        self.render_boosters = True
        self.projectiles = []

    def handle_inputs(self, event: pygame.event.Event):
        self.state_machine.handle_inputs(event)

    def update(self, dt: float) -> None:
        super().update(dt)
        self.boosters.x = self.x + settings.BOOSTERS_OFFSET_X
        self.boosters.y = self.y + settings.BOOSTERS_OFFSET_Y
        self.boosters.update(dt)

    def render(self, surface: pygame.Surface) -> None:
        super().render(surface)
        if self.render_boosters:
            self.boosters.render(surface)
