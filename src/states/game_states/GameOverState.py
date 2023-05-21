from typing import TypeVar

import pygame

import settings

from src.states.BaseState import BaseState
from src.utilities.text import render_text_img

class GameOverState(BaseState):
    def enter(self, game_level: TypeVar("GameLevel")) -> None:    
        settings.SOUNDS["gameover_loud"].play()
        self.game_level = game_level
        
    def handle_inputs(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            self.state_machine.change("start")

    def render(self, surface: pygame.Surface) -> None:
        render_text_img(surface, settings.TEXTURES["GAME_OVER"], settings.VIRTUAL_WIDTH // 2, settings.VIRTUAL_HEIGHT // 2, center=True)
        # score
        x = 0
        for digit in str(self.game_level.score)[::-1]:
            frame_index = int(digit)
            texture = settings.TEXTURES["number_font"]
            frame = settings.FRAMES["number_font"][frame_index - 1]
            surface.blit(texture, (settings.VIRTUAL_WIDTH // 2 + len(str(self.game_level.score)) - x, settings.VIRTUAL_HEIGHT // 2 + 8), frame)
            x += 8