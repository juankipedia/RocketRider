from typing import Optional

import pygame


def render_text(
    surface: pygame.Surface,
    text: str,
    font: pygame.font.Font,
    x: float,
    y: float,
    color: pygame.Color,
    bgcolor: Optional[pygame.Color] = None,
    center: bool = False,
    shadowed: bool = False,
):
    text_obj: pygame.Surface = font.render(text, True, color, bgcolor)
    text_rect: pygame.Rect = text_obj.get_rect()

    if center:
        text_rect.center = (x, y)
    else:
        text_rect.x = x
        text_rect.y = y

    if shadowed:
        shadow_text: pygame.Surface = font.render(text, True, (0, 0, 0))
        shadow_rect: pygame.Rect = shadow_text.get_rect()
        shadow_rect.x = text_rect.x + 1
        shadow_rect.y = text_rect.y + 1
        surface.blit(shadow_text, shadow_rect)

    surface.blit(text_obj, text_rect)


def render_text_img(
    surface: pygame.Surface,
    img: pygame.Surface,
    x: float,
    y: float,
    frame: pygame.Rect = None,
    center: bool = False,
):
    img_obj: pygame.Surface = img
    img_rect: pygame.Rect = img.get_rect()

    if center:
        img_rect.center = (x, y)
    else:
        img_rect.x = x
        img_rect.y = y

    if frame is not None:
        surface.blit(img_obj, img_rect, frame)
    else:
        surface.blit(img_obj, img_rect)
