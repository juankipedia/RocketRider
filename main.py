import settings

from src.Game import Game

if __name__ == "__main__":
    game = Game(
        "RocketRider",
        settings.WINDOW_WIDTH,
        settings.WINDOW_HEIGHT,
        settings.VIRTUAL_WIDTH,
        settings.VIRTUAL_HEIGHT,
    )
    game.exec()
