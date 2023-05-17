from typing import Sequence, Optional, Dict, Any

class Animation:
    def __init__(
        self,
        frames: Sequence[Any],
        time_interval: float = 0,
        loops: Optional[int] = None,
    ) -> None:
        self.frames: Sequence[Any] = frames
        self.interval: float = time_interval
        self.loops: Optional[int] = loops
        self.size: int = len(self.frames)
        self.timer: float = 0
        self.times_played: int = 0
        self.current_frame_index: int = 0

    def reset(self) -> None:
        self.times_played = 0
        self.timer = 0
        self.current_frame = 0

    def update(self, dt: float) -> None:
        if self.size <= 1 or (
            self.loops is not None and self.times_played > self.loops
        ):
            return

        self.timer += dt

        if self.timer >= self.interval:
            self.timer %= self.interval
            self.current_frame_index = (self.current_frame_index + 1) % self.size

            if self.current_frame_index == 0 and self.loops is not None:
                self.times_played += 1

    def get_current_frame(self) -> Any:
        return self.frames[self.current_frame_index]

class AnimatedMixin:
    def generate_animations(self, animation_defs: Dict[str, Dict[str, Any]]) -> None:
        for animation_id, values in animation_defs.items():
            animation = Animation(
                values["frames"],
                values.get("interval", 0),  # Given interval or zero
                loops=values.get("loops"),  # Given loops or None
            )
            self.animations[animation_id] = animation

    def change_animation(self, animation_id: str) -> None:
        new_animation = self.animations[animation_id]
        if new_animation != self.current_animation:
            self.current_animation = new_animation
            self.current_animation.reset()
            self.frame_index = self.current_animation.get_current_frame()

    def update(self, dt: float) -> None:
        self.current_animation.update(dt)
        self.frame_index = self.current_animation.get_current_frame()
