from typing import Any, Dict

import random
import pygame

import settings

from src.states.BaseState import BaseState
from src.Player import Player
from src.Enemy import Enemy
from src.Projectile import Projectile
from src.GameLevel import GameLevel
from src.Camera import Camera

class PlayState(BaseState):
    def enter(self, **params: Dict[str, Any]) -> None:
        self.level = params.get("level", 1)
        self.camera = params.get(
            "camera",
            Camera(
                0,
                0,
                settings.VIRTUAL_WIDTH,
                settings.VIRTUAL_HEIGHT,
            ),
        )

        self.player = params.get("player")
        if self.player is None:
            self.player = Player(settings.VIRTUAL_WIDTH // 2, settings.VIRTUAL_HEIGHT - settings.SPACESHIP_HEIGHT - settings.BOOSTERS_HEIGHT)
            self.player.change_state("idle")
        
        self.game_level = params.get("game_level")
        if self.game_level is None:
            self.game_level = GameLevel(1, self.camera, self.player)
            pygame.mixer_music.load(settings.BASE_DIR / "sounds" / "battle.wav")
            pygame.mixer_music.play(loops=-1)

    def exit(self) -> None:
        pygame.mixer_music.stop()

    def handle_inputs(self, event: pygame.event.Event):
        self.player.handle_inputs(event)

    def update(self, dt: float) -> None:
        if self.player.is_dead:
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            self.state_machine.change("game_over", self.game_level)

        self.player.update(dt)
        
        self.game_level.update(dt)

        for projectile in self.game_level.projectiles:
            if self.player.collides(projectile):
                settings.SOUNDS["hit_hurt"].play()
                projectile.on_collide(self.player)

        for projectile in self.player.projectiles:
            for enemy in self.game_level.enemies:
                if enemy.collides(projectile):
                    settings.SOUNDS["hit_hurt2"].play()
                    self.game_level.score += enemy.score_points
                    projectile.on_collide(enemy)


    def render(self, surface: pygame.Surface) -> None:
        self.game_level.render(surface)
        self.player.render(surface)
        surface.blit(surface, (-self.camera.x, -self.camera.y))
