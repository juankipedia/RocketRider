import random
import pygame

import settings

from src.Camera import Camera
from src.Player import Player
from src.Enemy import Enemy
from src.definitions import enemies

class GameLevel:
    def __init__(self, num_level: int, camera: Camera, player: Player) -> None:
        self.enemies = []
        self.projectiles = []
        self.num_level = num_level
        self.camera = camera
        self.player = player
        self.num_enemies = 1
        self.score = 0
        self.__generate_enemies()

    def __generate_enemies(self) -> None:
        types = ["alan", "bon_bon", "lips"]
        for _ in range(self.num_enemies):
            type = random.choice(types)
            definition = enemies.ENEMIES[type]
            x = random.randint(self.camera.x, self.camera.x + self.camera.width)
            y = -settings.ENEMY_HEIGHT
            self.enemies.append(
                Enemy(
                    x,
                    y,
                    settings.ENEMY_WIDTH,
                    settings.ENEMY_HEIGHT,
                    game_level=self,
                    **definition
                )
            )

    def update(self, dt: float) -> None:
        for enemy in self.enemies:
            enemy.update(dt)

        for projectile in self.projectiles:
            projectile.update(dt)
        
        for projectile in self.player.projectiles:
            projectile.update(dt)

        # Remove not in play projectiles
        self.player.projectiles = [
            projectile for projectile in self.player.projectiles if projectile.in_play
        ]

        # Remove dead enemies
        self.enemies = [
            enemy for enemy in self.enemies if not enemy.is_dead
        ]

        # Remove not in play projectiles
        self.projectiles = [
            projectile for projectile in self.projectiles if projectile.in_play
        ]

        if len(self.enemies) == 0:
            self.num_enemies *= 2
            self.__generate_enemies()

    def render(self, surface: pygame.Surface) -> None:
        for enemy in self.enemies:
            enemy.render(surface)

        for projectile in self.projectiles:
            projectile.render(surface)

        for projectile in self.player.projectiles:
            projectile.render(surface)

        # render HUD
        # score
        x = 0
        for digit in str(self.score)[::-1]:
            frame_index = int(digit)
            texture = settings.TEXTURES["number_font"]
            frame = settings.FRAMES["number_font"][frame_index - 1]
            surface.blit(texture, (settings.VIRTUAL_WIDTH - 8 - x, 0), frame)
            x += 8

        # life
        surface.blit(settings.TEXTURES["player_life_icon"], (settings.VIRTUAL_WIDTH - 16, settings.VIRTUAL_HEIGHT - 16))
        texture = settings.TEXTURES["number_font"]
        frame = settings.FRAMES["number_font"][self.player.hp - 1]
        surface.blit(settings.TEXTURES["number_font"], (settings.VIRTUAL_WIDTH - 16 - 8, settings.VIRTUAL_HEIGHT - 12), frame)

        
            