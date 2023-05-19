from typing import Dict, Any

from src.Projectile import Projectile
from src.GameEntity import GameEntity

def make_damage(projectile: Projectile, entity: GameEntity):
    projectile.in_play = False
    entity.hp -= projectile.damage
    if (entity.hp <= 0):
        entity.is_dead = True

PROJECTILES: Dict[str, Dict[str, Any]] = {
    "enemy_projectile_0": {
        "texture_id": "enemy_projectile",
        "animation_defs": {
            "shoot": {"frames": [0]},
        },
        "damage": 1,
        "solidness": dict(top=True, right=True, bottom=True, left=True),
        "on_collide": make_damage
    },
    "enemy_projectile_1": {
        "texture_id": "enemy_projectile",
        "animation_defs": {
            "shoot": {"frames": [1]},
        },
        "damage": 1,
        "solidness": dict(top=True, right=True, bottom=True, left=True),
        "on_collide": make_damage
    },
    "enemy_projectile_2": {
        "texture_id": "enemy_projectile",
        "animation_defs": {
            "shoot": {"frames": [2]},
        },
        "damage": 1,
        "solidness": dict(top=True, right=True, bottom=True, left=True),
        "on_collide": make_damage
    },
    "enemy_projectile_3": {
        "texture_id": "enemy_projectile",
        "animation_defs": {
            "shoot": {"frames": [3]},
        },
        "damage": 1,
        "solidness": dict(top=True, right=True, bottom=True, left=True),
        "on_collide": make_damage
    },
    "player_beam": {
        "texture_id": "player_beam",
        "animation_defs": {
            "shoot": {"frames": [0]},
        },
        "damage": 1,
        "solidness": dict(top=True, right=True, bottom=True, left=True),
        "on_collide": make_damage
    },
    "player_charged_beam" : {
        "texture_id": "player_charged_beam",
        "animation_defs": {
            "shoot": {"frames": [0, 1], "interval": 0.1},
        },
        "damage": 1,
        "solidness": dict(top=True, right=True, bottom=True, left=True),
        "on_collide": make_damage
    },
    "player_charged_donut_shot": {
        "texture_id": "player_charged_donut_shot",
        "animation_defs": {
            "shoot": {"frames": [0, 1, 2, 3], "interval": 0.1},
        },
        "damage": 1,
        "solidness": dict(top=True, right=True, bottom=True, left=True),
        "on_collide": make_damage
    },
    "player_charged_square_shot": {
        "texture_id": "player_charged_square_shot",
        "animation_defs": {
            "shoot": {"frames": [0, 1, 2, 3, 4, 5, 6, 7], "interval": 0.1},
        },
        "damage": 1,
        "solidness": dict(top=True, right=True, bottom=True, left=True),
        "on_collide": make_damage
    },
    "player_donut_shot": {
        "texture_id": "player_donut_shot",
        "animation_defs": {
            "shoot": {"frames": [0, 1], "interval": 0.1},
        },
        "damage": 1,
        "solidness": dict(top=True, right=True, bottom=True, left=True),
        "on_collide": make_damage
    },
    "player_missile_shots": {
        "texture_id": "player_missile_shots",
        "animation_defs": {
            "shoot": {"frames": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], "interval": 0.1},
        },
        "damage": 1,
        "solidness": dict(top=True, right=True, bottom=True, left=True),
        "on_collide": make_damage
    },
    "player_square_shot": {
        "texture_id": "player_square_shot",
        "animation_defs": {
            "shoot": {"frames": [0, 1, 2, 3], "interval": 0.1},
        },
        "damage": 1,
        "solidness": dict(top=True, right=True, bottom=True, left=True),
        "on_collide": make_damage,
    }
}