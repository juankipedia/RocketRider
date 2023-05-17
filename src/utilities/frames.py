from typing import List

import pygame

def generate_frames() -> List[pygame.Rect]:
    ship_size = 16
    x = 0

    frames = []

    for _ in range (3):
        frames.append(pygame.Rect(x, 0, ship_size, ship_size))
        x += ship_size
        
    return frames