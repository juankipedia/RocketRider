from typing import Callable, TypeVar, Any, Optional, Dict

from src.GameObject import GameObject


class Projectile(GameObject):
    def __init__(
        self,
        damage: float,
        on_collide: Optional[Callable[[TypeVar("Projectile"), Any], Any]] = None,
        *args,
        **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)
        self._on_collide = on_collide
        self.damage = damage
        self.in_play = True
        self.change_animation("shoot")

    def on_collide(self, another: Any) -> Any:
        if self._on_collide is None:
            return None
        return self._on_collide(self, another)
