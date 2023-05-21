from typing import Any, Dict, TypeVar

import settings

from src.GameEntity import GameEntity
from src.mixins import AnimatedMixin

class Enemy(GameEntity):
    def __init__(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
        game_level: TypeVar("GameLevel"),
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
        self.max_hp = settings.ENEMY_HP
        self.hp = self.max_hp
        self.walk_speed = definition["walk_speed"]
        self.projectile_id = definition.get("projectile_id")
        self.projectile_speed = definition.get("projectile_speed")
        self.score_points = definition.get("score_points")
        self.state_machine.change(definition["first_state"])
        self.exploited = False

    def __generate_states(self, states_definition: Dict[str, TypeVar("BaseState")]):
        states = {}
        for state_name, state_class in states_definition.items():

            def cb(state_class):
                states[state_name] = lambda sm: state_class(self, sm)

            cb(state_class)
        return states
    
    def update(self, dt: float) -> None:
        self.state_machine.update(dt)
        AnimatedMixin.update(self, dt)

        self.x = self.x + self.vx * dt
        self.y = self.y + self.vy * dt

        self.x = max(0, min(settings.WORLD_WIDTH - self.width, self.x))
        
        if (self.y >= settings.WORLD_HEIGHT):
            self.is_dead = True
            self.game_level.player.hp -= 1
            if (self.game_level.player.hp == 0):
                self.game_level.player.change_state("dead")
