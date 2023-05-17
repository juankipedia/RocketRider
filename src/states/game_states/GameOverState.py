from typing import Any, Dict, Tuple

import pygame

import settings

from src.states.BaseState import BaseState
from src.utilities.text import render_text_img

class GameOverState(BaseState):
    def enter(self, *args: Tuple[Any], **kwargs: Dict[str, Any]) -> None:
        self.win = kwargs.get("win", False)
        if self.win:
            settings.SOUNDS["win_loud"].play()
        else:
            settings.SOUNDS["gameover_loud"].play()

    def exit(self) -> None:
        pass

    def handle_inputs(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            self.state_machine.change("start")
    
    def render(self, surface: pygame.Surface) -> None:
        window_rect = settings.TEXTURES["window"].get_rect()
        score_rect = settings.TEXTURES["score"].get_rect()
        table_rect = settings.TEXTURES["table"].get_rect()
        record_rect = settings.TEXTURES["record"].get_rect()

        render_text_img(surface, settings.TEXTURES["window"], settings.VIRTUAL_WIDTH // 2, settings.VIRTUAL_HEIGHT // 2, center=True)
        
        if (self.win):
            render_text_img(surface, settings.TEXTURES["you_win"], settings.VIRTUAL_WIDTH // 2, 70, center=True)
        else:
            render_text_img(surface, settings.TEXTURES["you_lose"], settings.VIRTUAL_WIDTH // 2, 70, center=True)

        render_text_img(surface, settings.TEXTURES["replay_btn"], settings.VIRTUAL_WIDTH // 2 - window_rect.right // 2 + 40 + 143, window_rect.bottom - 40 - 105, center=True)
        render_text_img(surface, settings.TEXTURES["play_btn"], settings.VIRTUAL_WIDTH // 2 - window_rect.right // 2 + 40 + 143 + 286, window_rect.bottom - 40 - 105, center=True)
        render_text_img(surface, settings.TEXTURES["close_btn"], settings.VIRTUAL_WIDTH // 2 - window_rect.right // 2 + 40 + 143 + 286*2, window_rect.bottom - 40 - 105, center=True)

        render_text_img(surface, settings.TEXTURES["star03"], settings.VIRTUAL_WIDTH // 2 - window_rect.right // 2 + 40 + 146, 280 + 110, center=True)
        render_text_img(surface, settings.TEXTURES["star03"], settings.VIRTUAL_WIDTH // 2 - window_rect.right // 2 + 40 + 146 + 292, 280 + 55, center=True)
        render_text_img(surface, settings.TEXTURES["star01"], settings.VIRTUAL_WIDTH // 2 - window_rect.right // 2 + 40 + 146 + 292*2, 280 + 110, center=True)

        render_text_img(surface, settings.TEXTURES["score"], settings.VIRTUAL_WIDTH // 2 - score_rect.right // 2, settings.VIRTUAL_HEIGHT // 2 + score_rect.bottom, center=True)
        render_text_img(surface, settings.TEXTURES["table"], settings.VIRTUAL_WIDTH // 2 + table_rect.right // 2 + 40, settings.VIRTUAL_HEIGHT // 2 + table_rect.bottom // 2, center=True)

        render_text_img(surface, settings.TEXTURES["record"], settings.VIRTUAL_WIDTH // 2 - score_rect.right // 2, settings.VIRTUAL_HEIGHT // 2 + score_rect.bottom + record_rect.bottom * 2, center=True)
        render_text_img(surface, settings.TEXTURES["table"], settings.VIRTUAL_WIDTH // 2 + table_rect.right // 2 + 40, settings.VIRTUAL_HEIGHT // 2 + table_rect.bottom // 2 + table_rect.bottom, center=True)

