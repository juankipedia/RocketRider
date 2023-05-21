from typing import Dict, Any

from src.mixins import AnimatedMixin, CollidableMixin, DrawableMixin


class GameObject(AnimatedMixin, CollidableMixin, DrawableMixin):
    TOP = "top"
    RIGHT = "right"
    BOTTOM = "bottom"
    LEFT = "left"

    DEFAULT_SOLIDNESS = {TOP: False, RIGHT: False, BOTTOM: False, LEFT: False}

    def __init__(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
        texture_id: str,
        animation_defs: Dict[str, Dict[str, Any]],
        solidness: Dict[str, bool],
    ) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.texture_id = texture_id
        self.frame_index = -1
        self.current_animation = None
        self.animations = {}
        self.generate_animations(animation_defs)
        self.solidness = solidness
        self.flipped = False

    def collides_on(self, another: CollidableMixin, side: str) -> bool:
        return self.is_solid_on(side) and self.collides(another)

    def is_solid_on(self, side: str) -> bool:
        return self.solidness[side]
    
    def update(self, dt: float) -> None:
        AnimatedMixin.update(self, dt)
