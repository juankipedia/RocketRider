from pathlib import Path

import pygame

from src.utilities import generate_frames

# Window size
WINDOW_WIDTH = 464
WINDOW_HEIGHT = 928

# Virtual Window size
VIRTUAL_WIDTH = 116
VIRTUAL_HEIGHT = 232

# World dimensions
WORLD_WIDTH = 116
WORLD_HEIGHT = 232

# Background
SCROLL_SPEED = 50

# Spaceship
SPACESHIP_WIDTH = 16
SPACESHIP_HEIGHT = 16
SPACESHIP_HP = 3
SPACESHIP_SPEED = 100
SPACESHIP_PROYECTILE_SPEED = 300
SPACESHIP_PROYECTILE_WIDTH = 16
SPACESHIP_PROYECTILE_HEIGHT = 16
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
ENEMY_HP = 1
ENEMY_SPEED = 100
ENEMY_PROYECTILE_SPEED = 100
ENEMY_PROYECTILE_WIDTH = 16
ENEMY_PROYECTILE_HEIGHT = 16
ENEMY_DRAG_COEFFICIENT = 0.98
ENEMY_ATTACK_RANGE = 50

BASE_DIR = Path(__file__).parent

pygame.mixer.init()

SOUNDS = {
    "blip": pygame.mixer.Sound(BASE_DIR / "sounds" / "blip.wav"),
    "select": pygame.mixer.Sound(BASE_DIR / "sounds" / "select.wav"),
    "gameover_loud": pygame.mixer.Sound(BASE_DIR / "sounds" / "gameover_loud.mp3"),
    "win_loud": pygame.mixer.Sound(BASE_DIR / "sounds" / "win_loud.mp3"),
    "laser_shoot": pygame.mixer.Sound(BASE_DIR / "sounds" / "laser_shoot.wav"),
    "laser_shoot2": pygame.mixer.Sound(BASE_DIR / "sounds" / "laser_shoot2.wav"),
    "hit_hurt": pygame.mixer.Sound(BASE_DIR / "sounds" / "hit_hurt.wav"),
    "hit_hurt2": pygame.mixer.Sound(BASE_DIR / "sounds" / "hit_hurt2.wav")
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
    "enemy_projectile": pygame.image.load(BASE_DIR / "graphics" / "enemy_projectile.png"),
    "player_beam": pygame.image.load(BASE_DIR / "graphics" / "player_beam.png"),
    "player_charged_beam": pygame.image.load(BASE_DIR / "graphics" / "player_charged_beam.png"),
    "player_charged_donut_shot": pygame.image.load(BASE_DIR / "graphics" / "player_charged_donut_shot.png"),
    "player_charged_square_shot": pygame.image.load(BASE_DIR / "graphics" / "player_charged_square_shot.png"),
    "player_donut_shot": pygame.image.load(BASE_DIR / "graphics" / "player_donut_shot.png"),
    "player_missile_shots": pygame.image.load(BASE_DIR / "graphics" / "player_missile_shots.png"),
    "player_square_shot": pygame.image.load(BASE_DIR / "graphics" / "player_square_shot.png"),
    "explosion": pygame.image.load(BASE_DIR / "graphics" / "explosion.png"),
    "sparkle": pygame.image.load(BASE_DIR / "graphics" / "sparkle.png"),
    "START": pygame.image.load(BASE_DIR / "graphics" / "START.png"),
    "GAME_OVER": pygame.image.load(BASE_DIR / "graphics" / "GAME_OVER.png"),
    "player_life_icon": pygame.image.load(BASE_DIR / "graphics" / "player_life_icon.png"),
    "number_font": pygame.image.load(BASE_DIR / "graphics" / "number_font.png"),
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
    "window": pygame.image.load(BASE_DIR / "graphics" / "window.png")
}

FRAMES = {
    "spaceship": generate_frames(1, 3, SPACESHIP_WIDTH, SPACESHIP_HEIGHT),
    "boosters": generate_frames(1, 3, BOOSTERS_WIDTH, BOOSTERS_HEIGHT),
    "boosters_left": generate_frames(1, 3, BOOSTERS_WIDTH, BOOSTERS_HEIGHT),
    "boosters_right": generate_frames(1, 3, BOOSTERS_WIDTH, BOOSTERS_HEIGHT),
    "alan": generate_frames(1, 6, ENEMY_WIDTH, ENEMY_HEIGHT),
    "bon_bon": generate_frames(1, 4, ENEMY_WIDTH, ENEMY_HEIGHT),
    "lips": generate_frames(1, 5, ENEMY_WIDTH, ENEMY_HEIGHT),
    "enemy_projectile": generate_frames(1, 4, ENEMY_PROYECTILE_WIDTH, ENEMY_PROYECTILE_HEIGHT),
    "player_beam": generate_frames(1, 1, SPACESHIP_PROYECTILE_WIDTH, SPACESHIP_PROYECTILE_HEIGHT),
    "player_charged_beam": generate_frames(1, 2, SPACESHIP_PROYECTILE_WIDTH, SPACESHIP_PROYECTILE_HEIGHT),
    "player_charged_donut_shot": generate_frames(1, 4, SPACESHIP_PROYECTILE_WIDTH, SPACESHIP_PROYECTILE_HEIGHT),
    "player_charged_square_shot": generate_frames(1, 8, SPACESHIP_PROYECTILE_WIDTH, SPACESHIP_PROYECTILE_HEIGHT),
    "player_donut_shot": generate_frames(1, 2, SPACESHIP_PROYECTILE_WIDTH, SPACESHIP_PROYECTILE_HEIGHT),
    "player_missile_shots": generate_frames(1, 16, SPACESHIP_PROYECTILE_WIDTH, SPACESHIP_PROYECTILE_HEIGHT),
    "player_square_shot": generate_frames(1, 4, SPACESHIP_PROYECTILE_WIDTH, SPACESHIP_PROYECTILE_HEIGHT),
    "explosion": generate_frames(1, 6, ENEMY_WIDTH, ENEMY_HEIGHT),
    "sparkle": generate_frames(1, 5, ENEMY_WIDTH, ENEMY_HEIGHT),
    "number_font": generate_frames(2, 5, 8, 8),
    "player_life_icon": generate_frames(1, 1, 16, 16)

}

pygame.font.init()

FONTS = {}
