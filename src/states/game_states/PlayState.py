from typing import Any, Dict

import pygame

import settings

from src.states.BaseState import BaseState
from src.Player import Player
# from src.space_object import SpaceObject
# from src.spacecraft import Spacecraft
# from src.enemy import Enemy
# from src.projectile import Projectile

  
class PlayState(BaseState):
    def enter(self, **params: Dict[str, Any]) -> None:
        self.player = params.get("player")
        if self.player is None:
            self.player = Player(settings.VIRTUAL_WIDTH // 2, settings.VIRTUAL_HEIGHT // 2, None)
            self.player.change_state("idle")

        # self.enemy_projectiles = pygame.sprite.Group()
        # self.all_sprites = pygame.sprite.Group()
        # self.enemy = Enemy(settings.VIRTUAL_WIDTH, settings.VIRTUAL_HEIGHT, self.spacecraft, self.enemy_projectiles, self.all_sprites)
        # self.player_projectiles = pygame.sprite.Group()
        # self.all_sprites.add(self.spacecraft)
        # self.all_sprites.add(self.enemy)
        # self.camera_x, self.camera_y = 0, 0

        pygame.mixer_music.load(settings.BASE_DIR / "sounds" / "battle.wav")
        pygame.mixer_music.play(loops=-1)

    def exit(self) -> None:
        pygame.mixer_music.stop()

    def handle_inputs(self, event: pygame.event.Event):
        self.player.handle_inputs(event)

    def update(self, dt: float) -> None:
        self.player.update(dt)

        # self.all_sprites.update(dt)

        # self.camera_x, self.camera_y = get_camera_position(self.spacecraft, settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT, settings.WORLD_WIDTH, settings.WORLD_HEIGHT, self.camera_x, self.camera_y)

        # for proj in self.enemy_projectiles:
        #     if self.spacecraft.rect.colliderect(proj.rect):
        #         proj.kill()
        #         self.spacecraft.take_damage(2)
        #         if self.spacecraft.hp <= 0:
        #             self.spacecraft.kill()
        #             self.state_machine.change("game_over", win=False)

        # for proj in self.player_projectiles:
        #     if self.enemy.rect.colliderect(proj.rect):
        #         proj.kill()
        #         self.enemy.take_damage(2)
        #         if self.enemy.hp <= 0:
        #             self.enemy.kill()
        #             self.state_machine.change("game_over", win=True)
        pass

    def render(self, surface: pygame.Surface) -> None:
        self.player.render(surface)
        # surface.blit(self.spacecraft.image, (0, 0), settings.FRAMES["ship"][1])
        # for sprite in self.all_sprites:
        #     surface.blit(sprite.image, sprite.rect.move(self.camera_x, self.camera_y))
        #     if isinstance(sprite, SpaceObject):
        #         sprite.draw_health_bar(surface, self.camera_x, self.camera_y)
        pass