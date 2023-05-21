from typing import TypeVar, Tuple, Dict, Any

import pygame

import settings

from src.states.BaseState import BaseState
from src.utilities.text import render_text_img

class StartState(BaseState):
    def enter(self) -> None:
        self.selected = 0
        
        pygame.mixer_music.load(settings.BASE_DIR / "sounds" / "menu.wav")
        pygame.mixer_music.play(loops=-1)

    def exit(self) -> None:
        pygame.mixer_music.stop()

    def handle_inputs(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            settings.SOUNDS["select"].play()
            self.state_machine.change("play")

        self.selected = max(0, min(self.selected, 1))

    def render(self, surface: pygame.Surface) -> None:
        render_text_img(surface, settings.TEXTURES["START"], settings.VIRTUAL_WIDTH // 2, settings.VIRTUAL_HEIGHT // 2, center=True)