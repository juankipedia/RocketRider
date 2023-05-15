from typing import TypeVar, Tuple, Dict, Any

import pygame

import settings

from .BaseState import BaseState
from src.utilities.text import render_text_img

class StartState(BaseState):
    def enter(self, *args: Tuple[Any], **kwargs: Dict[str, Any]) -> None:
        self.selected = 0
        pygame.mixer_music.load(settings.BASE_DIR / "sounds" / "menu.wav")
        pygame.mixer_music.play(loops=-1)

    def exit(self) -> None:
        pygame.mixer_music.stop()

    def handle_inputs(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.selected += 1
                settings.SOUNDS["blip"].play()
            elif event.key == pygame.K_UP:
                self.selected -=1
                settings.SOUNDS["blip"].play()
            elif event.key == pygame.K_RETURN and self.selected == 0:
                settings.SOUNDS["select"].play()
                self.state_machine.change("play")

        self.selected = max(0, min(self.selected, 2))

    def render(self, surface: pygame.Surface) -> None:
        render_text_img(surface, settings.TEXTURES["header"], settings.VIRTUAL_WIDTH // 2, settings.VIRTUAL_HEIGHT * 0.35, center=True)
        render_text_img(surface, settings.TEXTURES["start_btn"], settings.VIRTUAL_WIDTH // 2, settings.VIRTUAL_HEIGHT - 363, center=True)
        render_text_img(surface, settings.TEXTURES["map_btn"], settings.VIRTUAL_WIDTH // 2, settings.VIRTUAL_HEIGHT - 242, center=True)
        render_text_img(surface, settings.TEXTURES["exit_btn"], settings.VIRTUAL_WIDTH // 2, settings.VIRTUAL_HEIGHT - 121, center=True)
        render_text_img(surface, settings.TEXTURES["info_btn"], 105, 105, center=True)
        render_text_img(surface, settings.TEXTURES["settings_btn"], settings.VIRTUAL_WIDTH - 105, 105, center=True)
        render_text_img(surface, settings.TEXTURES["faq_btn"], settings.VIRTUAL_WIDTH - 105, settings.VIRTUAL_HEIGHT - 105, center=True)
        render_text_img(surface, settings.TEXTURES["rating_btn"], 105, settings.VIRTUAL_HEIGHT - 105, center=True)
        if self.selected == 0:
            render_text_img(surface, settings.TEXTURES["arrow"], settings.VIRTUAL_WIDTH // 2 - 210 - 47, (settings.VIRTUAL_HEIGHT - 363), center=True)
        elif self.selected == 1:
            render_text_img(surface, settings.TEXTURES["arrow"], settings.VIRTUAL_WIDTH // 2 - 210 - 47, (settings.VIRTUAL_HEIGHT - 242), center=True)
        elif self.selected == 2:
            render_text_img(surface, settings.TEXTURES["arrow"], settings.VIRTUAL_WIDTH // 2 - 210 - 47, (settings.VIRTUAL_HEIGHT - 121), center=True)
