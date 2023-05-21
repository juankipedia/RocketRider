from typing import List

import pygame

def generate_frames(rows: int, cols: int, tile_width: int, tile_height: int) -> List[pygame.Rect]:
    x = 0
    y = 0

    frames = []

    for _ in range(rows):
        for _ in range (cols):
            frames.append(pygame.Rect(x, y, tile_width, tile_height))
            x += tile_width
        x = 0
        y += tile_height
            
    return frames