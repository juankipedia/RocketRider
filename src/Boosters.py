from typing import Any, Dict, TypeVar

from src.mixins import AnimatedMixin, DrawableMixin


class Boosters(AnimatedMixin, DrawableMixin):
    def __init__(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
        texture_id: str,
        animation_defs: Dict[str, Dict[str, Any]],
    ) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.texture_id = texture_id
        self.frame_index = -1
        self.flipped = False
        self.current_animation = None
        self.animations = {}
        self.generate_animations(animation_defs)
