from typing import Any, Dict

import random
import pygame

import settings

from src.states.BaseState import BaseState
from src.Player import Player
from src.Enemy import Enemy
from src.definitions import enemies


class PlayState(BaseState):
    def enter(self, **params: Dict[str, Any]) -> None:
        self.player = params.get("player")
        if self.player is None:
            self.player = Player(
                settings.VIRTUAL_WIDTH // 2, settings.VIRTUAL_HEIGHT // 2, None
            )
            self.player.change_state("idle")

        self.enemies = params.get("enemies")
        if self.enemies is None:
            self.enemies = []
            types = ["alan", "bon_bon", "lips"]
            for _ in range(10):
                type = random.choice(types)
                definition = enemies.ENEMIES[type]
                x = random.randint(0, settings.VIRTUAL_WIDTH)
                y = random.randint(0, settings.VIRTUAL_HEIGHT)
                self.enemies.append(
                    Enemy(
                        x,
                        y,
                        settings.ENEMY_WIDTH,
                        settings.ENEMY_HEIGHT,
                        None,
                        self.player,
                        **definition
                    )
                )

        pygame.mixer_music.load(settings.BASE_DIR / "sounds" / "battle.wav")
        pygame.mixer_music.play(loops=-1)

    def exit(self) -> None:
        pygame.mixer_music.stop()

    def handle_inputs(self, event: pygame.event.Event):
        self.player.handle_inputs(event)

    def update(self, dt: float) -> None:
        self.player.update(dt)
        for enemy in self.enemies:
            enemy.update(dt)

    def render(self, surface: pygame.Surface) -> None:
        self.player.render(surface)
        for enemy in self.enemies:
            enemy.render(surface)
