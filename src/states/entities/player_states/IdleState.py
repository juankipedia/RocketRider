from typing import TypeVar

import pygame

import settings

from src.states.entities.BaseEntityState import BaseEntityState


class IdleState(BaseEntityState):
    def enter(self) -> None:
        self.entity.vx = 0
        self.entity.vy = 0
        self.entity.change_animation("idle")
        self.entity.boosters.texture_id = "boosters"

    def exit(self) -> None:
        pass

    def handle_inputs(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.entity.change_state("move", "up")
            elif event.key == pygame.K_LEFT:
                self.entity.change_state("move", "left")
            elif event.key == pygame.K_DOWN:
                self.entity.change_state("move", "down")
            elif event.key == pygame.K_RIGHT:
                self.entity.change_state("move", "right")
            elif event.key == pygame.K_SPACE:
                self.entity.change_state("attack")