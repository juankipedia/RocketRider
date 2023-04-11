def lerp(a, b, t):
    return a + (b - a) * t

def get_camera_position(spacecraft, SCREEN_WIDTH, SCREEN_HEIGHT, WORLD_WIDTH, WORLD_HEIGHT, camera_x, camera_y, smoothness=0.05):
    target_x = -spacecraft.rect.x + SCREEN_WIDTH // 2
    target_y = -spacecraft.rect.y + SCREEN_HEIGHT // 2

    target_x = min(0, target_x)
    target_y = min(0, target_y)
    target_x = max(-(WORLD_WIDTH - SCREEN_WIDTH), target_x)
    target_y = max(-(WORLD_HEIGHT - SCREEN_HEIGHT), target_y)

    x = lerp(camera_x, target_x, smoothness)
    y = lerp(camera_y, target_y, smoothness)

    return round(x), round(y)
