from typing import TypeVar

from src.states.BaseState import BaseState
from src.states.StateMachine import StateMachine


class BaseEntityState(BaseState):
    def __init__(
        self, entity: TypeVar("GameEntity"), state_machine: StateMachine
    ) -> None:
        super().__init__(state_machine)
        self.entity = entity
