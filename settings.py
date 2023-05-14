from pathlib import Path

import pygame

# Window size
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080

# Virtual Window size
VIRTUAL_WIDTH = 1920
VIRTUAL_HEIGHT = 1080

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

SOUNDS = {
    "blip_select": pygame.mixer.Sound(BASE_DIR / "sounds" / "blip_Select.wav"),
    "ready": pygame.mixer.Sound(BASE_DIR / "sounds" / "ready.mp3"),
}

TEXTURES = {
    "bg_main_menu": pygame.image.load(
        BASE_DIR / "graphics" / "background.jpg"
    ),
    "header": pygame.image.load(BASE_DIR / "graphics" / "gui" / "header.png"),
    "start_btn": pygame.image.load(BASE_DIR / "graphics" / "gui" / "start_btn.png"),
    "exit_btn": pygame.image.load(BASE_DIR / "graphics" / "gui" / "exit_btn.png"),
    "map_btn": pygame.image.load(BASE_DIR / "graphics" / "gui" / "map_btn.png"),
    "info_btn": pygame.image.load(BASE_DIR / "graphics" / "gui" / "info_btn.png"),
    "rating_btn": pygame.image.load(BASE_DIR / "graphics" / "gui" / "rating_btn.png"),
    "settings_btn": pygame.image.load(
        BASE_DIR / "graphics" / "gui" / "settings_btn.png"
    ),
    "faq_btn": pygame.image.load(BASE_DIR / "graphics" / "gui" / "faq_btn.png"),
    "arrow": pygame.image.load(BASE_DIR / "graphics" / "gui" / "arrow.png"),
    "close_btn": pygame.image.load(BASE_DIR / "graphics" / "close_btn.png"),
    "record": pygame.image.load(BASE_DIR / "graphics" / "record.png"),
    "replay_btn": pygame.image.load(BASE_DIR / "graphics" / "replay_btn.png"),
    "score": pygame.image.load(BASE_DIR / "graphics" / "score.png"),
    "star01": pygame.image.load(BASE_DIR / "graphics" / "star01.png"),
    "star02": pygame.image.load(BASE_DIR / "graphics" / "star02.png"),
    "star03": pygame.image.load(BASE_DIR / "graphics" / "star03.png"),
    "you_lose": pygame.image.load(BASE_DIR / "graphics" / "you_lose.png"),
    "you_win": pygame.image.load(BASE_DIR / "graphics" / "you_win.png"),
    "play_btn": pygame.image.load(BASE_DIR / "graphics" / "play_btn.png"),
    "table": pygame.image.load(BASE_DIR / "graphics" / "table.png"),
    "window": pygame.image.load(BASE_DIR / "graphics" / "window.png"),
    "background": pygame.image.load(BASE_DIR / "graphics" / "background.jpg"),
    "spacecraft": pygame.image.load(BASE_DIR / "graphics" / "spacecraft.png"),
    "enemy": pygame.image.load(BASE_DIR / "graphics" / "enemy.png"),
}

FRAMES = {}

pygame.font.init()

FONTS = {}
