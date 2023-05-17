from typing import TypeVar

import pygame

import settings

from src.states.entities.BaseEntityState import BaseEntityState


class MoveState(BaseEntityState):
    def enter(self, direction: str) -> None:
        if direction == "up":
            self.entity.vx = 0
            self.entity.vy = -settings.SPACESHIP_ACCELERATION
        elif direction == "left":
            self.entity.vx = -settings.SPACESHIP_ACCELERATION
            self.entity.vy = 0
            self.entity.change_animation("move_left")
            self.entity.boosters.texture_id = "boosters_left"
        elif direction == "down":
            self.entity.vx = 0
            self.entity.vy = settings.SPACESHIP_ACCELERATION
        elif direction == "right":
            self.entity.vx = settings.SPACESHIP_ACCELERATION
            self.entity.vy = 0
            self.entity.change_animation("move_right")
            self.entity.boosters.texture_id = "boosters_right"

    def exit(self) -> None:
        pass

    def handle_inputs(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.entity.vx = 0
                self.entity.vy = -settings.SPACESHIP_ACCELERATION
                self.entity.boosters.texture_id = "boosters"
            elif event.key == pygame.K_LEFT:
                self.entity.vx = -settings.SPACESHIP_ACCELERATION
                self.entity.vy = 0
                self.entity.change_animation("move_left")
                self.entity.boosters.texture_id = "boosters_left"
            elif event.key == pygame.K_DOWN:
                self.entity.vx = 0
                self.entity.vy = settings.SPACESHIP_ACCELERATION
                self.entity.boosters.texture_id = "boosters_left"
            elif event.key == pygame.K_RIGHT:
                self.entity.vx = settings.SPACESHIP_ACCELERATION
                self.entity.vy = 0
                self.entity.change_animation("move_right")
                self.entity.boosters.texture_id = "boosters_right"

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.entity.change_state("idle")
            elif event.key == pygame.K_DOWN:
                self.entity.change_state("idle")
            elif event.key == pygame.K_LEFT:
                self.entity.change_state("idle")
            elif event.key == pygame.K_RIGHT:
                self.entity.change_state("idle")

    def update(self, dt: float) -> None:
        pass
