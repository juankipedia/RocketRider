from typing import Any, Dict, TypeVar

from src.GameEntity import GameEntity
from src.states.entities.enemy_states import PatrollState, ChaseState


class Enemy(GameEntity):
    def __init__(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
        game_level: TypeVar("GameLevel"),
        player: TypeVar("Player"),
        **definition
    ) -> None:
        super().__init__(
            x,
            y,
            width,
            height,
            definition["texture_id"],
            game_level,
            states=self.__generate_states(definition["states"]),
            animation_defs=definition["animation_defs"],
        )
        self.walk_speed = definition["walk_speed"]
        self.state_machine.change(definition["first_state"], self.flipped)
        self.player = player

    def __generate_states(self, states_definition: Dict[str, TypeVar("BaseState")]):
        states = {}
        for state_name, state_class in states_definition.items():

            def cb(state_class):
                states[state_name] = lambda sm: state_class(self, sm)

            cb(state_class)
        return states
