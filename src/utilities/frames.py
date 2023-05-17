from typing import List

import pygame

def generate_frames(cols: int, tile_width: int, tile_height: int) -> List[pygame.Rect]:
    x = 0

    frames = []

    for _ in range (cols):
        frames.append(pygame.Rect(x, 0, tile_width, tile_height))
        x += tile_width
        
    return frames