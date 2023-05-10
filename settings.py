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

# Spacecraft
SPACECRAFT_ACCELERATION = 600
SPACECRAFT_HP = 100
SPACECRAFT_PROYECTILE_SPEED = 100
SPACECRAFT_DRAG_COEFFICIENT = 0.98
SPACECRAFT_ROTATION_DEGREES = 3.0

# Enemy
ENEMY_ACCELERATION = 200
ENEMY_HP = 50
ENEMY_PROYECTILE_SPEED = 100
ENEMY_DRAG_COEFFICIENT = 0.98
ENEMY_ATTACK_RANGE = 300

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