from pathlib import Path

import pygame

# Size of our actual window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Size we are trying to emulate
VIRTUAL_WIDTH = 432
VIRTUAL_HEIGHT = 243

# World dimensions
WORLD_WIDTH = 1920
WORLD_HEIGHT = 1080

BASE_DIR = Path(__file__).parent

pygame.mixer.init()

SOUNDS = {}

TEXTURES = {
    "background": pygame.image.load(BASE_DIR / "graphics" / "background.jpg"),
    "spacecraft": pygame.image.load(BASE_DIR / "graphics" / "spacecraft.png"),
    "enemy": pygame.image.load(BASE_DIR / "graphics" / "enemy.png"),
}

FRAMES = {}

pygame.font.init()

FONTS = {}