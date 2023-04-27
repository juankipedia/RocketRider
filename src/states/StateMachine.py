from typing import Dict, Tuple, Any

import pygame

from .BaseState import BaseState

class StateMachine:
    def __init__(self, states: Dict[str, BaseState] = {}) -> None:
        self.states: Dict[str, BaseState] = states
        self.current = BaseState(self)

    def change(
        self, state_name: str, *args: Tuple[Any], **kwargs: Dict[str, Any]
    ) -> None:
        self.current.exit()
        self.current = self.states[state_name](self)
        self.current.enter(*args, **kwargs)

    def update(self, dt: float) -> None:
        self.current.update(dt)

    def render(self, surface: pygame.Surface) -> None:
        self.current.render(surface)

    