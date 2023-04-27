from typing import TypeVar, Tuple, Dict, Any

import pygame

class BaseState:
    def __init__(self, state_machine: TypeVar("StateMachine")) -> None:
        self.state_machine: TypeVar("StateMachine") = state_machine

    def enter(self, *args: Tuple[Any], **kwargs: Dict[str, Any]) -> None:
        pass

    def exit(self) -> None:
        pass

    def update(self, dt: float) -> None:
        pass

    def render(self, surface: pygame.Surface) -> None:
        pass