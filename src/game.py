import sys

from typing import Optional, Tuple, Dict, Any

import pygame

import settings
from src.states.StateMachine import StateMachine
from src.states.game_states import PlayState, StartState, GameOverState

pygame.init()

class Game:
    def __init__(
        self,
        title: Optional[str] = None,
        window_width: int = 800,
        window_height: int = 600,
        virtual_width: Optional[int] = None,
        virtual_height: Optional[int] = None,
        fps: int = 60,
        *args: Tuple[Any],
        **kwargs: Dict[str, Any]
    ) -> None:
        self.window_width: int = window_width
        self.window_height: int = window_height
        self.virtual_width: int = virtual_width or self.window_width
        self.virtual_height: int = virtual_height or self.window_height
        self.fps = fps

        # Setting the screen
        self.screen: pygame.Surface = pygame.display.set_mode(
            (self.window_width, self.window_height), *args, **kwargs
        )
        self.title: str = title or "Game"
        pygame.display.set_caption(self.title)

        # Creating the virtual screen
        self.render_surface = pygame.Surface((self.virtual_width, self.virtual_height))
        self.clock = pygame.time.Clock()
        
        # Creating the background surface
        self.background_surface = pygame.Surface((self.virtual_width, self.virtual_height * 2))
        background_width = settings.TEXTURES["background"].get_width()
        background_height = settings.TEXTURES["background"].get_height()

        for k in range(2):
            for x in range(0, self.virtual_width, background_width):
                for y in range(0, self.virtual_height, background_height):
                    self.background_surface.blit(settings.TEXTURES["background"], (x, k * self.virtual_height + y))
        
        self.background_y = self.virtual_height

        self.running: bool = False

        self.init()

    def init(self) -> None:
        self.state_machine = StateMachine(
            {"play": PlayState, "start": StartState, "game_over": GameOverState}
        )

        self.state_machine.change("play")

    def handle_inputs(self, event: pygame.event.Event):
        self.state_machine.handle_inputs(event)

    def update(self, dt: float) -> None:
        self.state_machine.update(dt)

    def render(self, render_surface: pygame.Surface) -> None:
        render_surface.blit(self.background_surface, (0, -self.background_y))
        self.state_machine.render(render_surface)

    def __update(self, dt: float) -> None:
        self.background_y -= settings.SCROLL_SPEED * dt

        if self.background_y < 0:
            self.background_y = self.virtual_height
        
        self.update(dt)

    def __render(self) -> None:
        self.render_surface.fill((0, 0, 0))
        self.render(self.render_surface)
        self.screen.blit(
            pygame.transform.scale(self.render_surface, self.screen.get_size()), (0, 0)
        )
        pygame.display.update()

    def exec(self) -> None:
        self.running = True

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                else:
                    self.handle_inputs(event)

            dt = self.clock.tick(self.fps) / 1000.0
            self.__update(dt)
            self.__render()

        pygame.font.quit()
        pygame.mixer.quit()
        pygame.quit()

    def quit(self) -> None:
        self.running = False
