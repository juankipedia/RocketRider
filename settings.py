from pathlib import Path

import pygame

from src.utilities import generate_frames

# Window size
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

# Virtual Window size
VIRTUAL_WIDTH = 512
VIRTUAL_HEIGHT = 288

# World dimensions
WORLD_WIDTH = 1920
WORLD_HEIGHT = 1080

# Background
SCROLL_SPEED = 50

# Spaceship
SPACESHIP_WIDTH = 16
SPACESHIP_HEIGHT = 16
SPACESHIP_HP = 100
SPACESHIP_ACCELERATION = 100
SPACESHIP_PROYECTILE_SPEED = 100
SPACESHIP_DRAG_COEFFICIENT = 0.98
SPACESHIP_ROTATION_DEGREES = 3

# Boosters
BOOSTERS_WIDTH = 16
BOOSTERS_HEIGHT = 16
BOOSTERS_OFFSET_X = 0.0
BOOSTERS_OFFSET_Y = 15.0

# Enemy
ENEMY_WIDTH = 16
ENEMY_HEIGHT = 16
ENEMY_HP = 50
ENEMY_ACCELERATION = 200
ENEMY_PROYECTILE_SPEED = 100
ENEMY_DRAG_COEFFICIENT = 0.98
ENEMY_ATTACK_RANGE = 300

BASE_DIR = Path(__file__).parent

pygame.mixer.init()

SOUNDS = {
    "blip": pygame.mixer.Sound(BASE_DIR / "sounds" / "blip.wav"),
    "select": pygame.mixer.Sound(BASE_DIR / "sounds" / "select.wav"),
    "gameover_loud": pygame.mixer.Sound(BASE_DIR / "sounds" / "gameover_loud.mp3"),
    "win_loud": pygame.mixer.Sound(BASE_DIR / "sounds" / "win_loud.mp3"),
}

TEXTURES = {
    "background": pygame.image.load(BASE_DIR / "graphics" / "background.png"),
    "spaceship": pygame.image.load(BASE_DIR / "graphics" / "spaceship.png"),
    "boosters": pygame.image.load(BASE_DIR / "graphics" / "boosters.png"),
    "boosters_left": pygame.image.load(BASE_DIR / "graphics" / "boosters_left.png"),
    "boosters_right": pygame.image.load(BASE_DIR / "graphics" / "boosters_right.png"),
    "alan": pygame.image.load(BASE_DIR / "graphics" / "alan.png"),
    "bon_bon": pygame.image.load(BASE_DIR / "graphics" / "bon_bon.png"),
    "lips": pygame.image.load(BASE_DIR / "graphics" / "lips.png"),
    "header": pygame.image.load(BASE_DIR / "graphics" / "header.png"),
    "start_btn": pygame.image.load(BASE_DIR / "graphics" / "start_btn.png"),
    "exit_btn": pygame.image.load(BASE_DIR / "graphics" / "exit_btn.png"),
    "map_btn": pygame.image.load(BASE_DIR / "graphics" / "map_btn.png"),
    "info_btn": pygame.image.load(BASE_DIR / "graphics" / "info_btn.png"),
    "rating_btn": pygame.image.load(BASE_DIR / "graphics" / "rating_btn.png"),
    "settings_btn": pygame.image.load(BASE_DIR / "graphics" / "settings_btn.png"),
    "faq_btn": pygame.image.load(BASE_DIR / "graphics" / "faq_btn.png"),
    "arrow": pygame.image.load(BASE_DIR / "graphics" / "arrow.png"),
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
}

FRAMES = {
    "spaceship": generate_frames(3, SPACESHIP_WIDTH, SPACESHIP_HEIGHT),
    "boosters": generate_frames(3, BOOSTERS_WIDTH, BOOSTERS_HEIGHT),
    "boosters_left": generate_frames(3, BOOSTERS_WIDTH, BOOSTERS_HEIGHT),
    "boosters_right": generate_frames(3, BOOSTERS_WIDTH, BOOSTERS_HEIGHT),
    "alan": generate_frames(6, ENEMY_WIDTH, ENEMY_HEIGHT),
    "bon_bon": generate_frames(4, ENEMY_WIDTH, ENEMY_HEIGHT),
    "lips": generate_frames(5, ENEMY_WIDTH, ENEMY_HEIGHT)
}

pygame.font.init()

FONTS = {}
