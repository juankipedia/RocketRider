from typing import Callable, TypeVar, Any, Optional, Dict

import pygame

import settings

from src.GameObject import GameObject


class Projectile(GameObject):
    def __init__(
        self,
        damage: float,
        on_collide: Optional[Callable[[TypeVar("Projectile"), Any], Any]] = None,
        vx: float = 0.0,
        vy: float = 0.0,
        *args,
        **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)
        self._on_collide = on_collide
        self.damage = damage
        self.vx = vx
        self.vy = vy
        self.in_play = True
        self.change_animation("shoot")

    def on_collide(self, another: Any) -> Any:
        if self._on_collide is None:
            return None
        return self._on_collide(self, another)
    
    def update(self, dt: float) -> None:
        super().update(dt)
        
        self.y = self.y + self.vy * dt
        
        if (self.y <= -self.height):
            self.in_play = False

    def render(self, surface: pygame.Surface) -> None:
        super().render(surface)


