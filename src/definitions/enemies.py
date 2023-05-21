from typing import Dict, Any

import settings

from src.states.entities import enemy_states

ENEMIES: Dict[str, Dict[str, Any]] = {
    "alan": {
        "texture_id": "alan",
        "walk_speed": 50,
        "animation_defs": {
            "idle": {"frames": [0, 1], "interval": 0.1},
            "walk": {"frames": [0, 1, 2, 3, 4, 5], "interval": 0.1},
            "dead": {"frames": [0, 1, 2, 3, 4, 5], "interval": 0.1}
        },
        "states": {
            "chase": enemy_states.ChaseState,
            "dead": enemy_states.DeadState
        },
        "first_state": "chase",
        "score_points": 5
    },
    "bon_bon": {
        "texture_id": "bon_bon",
        "walk_speed": 30,
        "animation_defs": {
            "idle": {"frames": [0, 1], "interval": 0.1},
            "walk": {"frames": [0, 1, 2, 3], "interval": 0.1},
            "dead": {"frames": [0, 1, 2, 3, 4, 5], "interval": 0.1}
        },
        "states": {
            "patroll": enemy_states.PatrollState,
            "attack": enemy_states.AttackState,
            "dead": enemy_states.DeadState
        },
        "first_state": "patroll",
        "projectile_id": "enemy_projectile_3",
        "projectile_speed": 100,
        "score_points": 1
    },
    "lips": {
        "texture_id": "lips",
        "walk_speed": 30,
        "animation_defs": {
            "idle": {"frames": [0, 1], "interval": 0.1},
            "walk": {"frames": [0, 1, 2, 3, 4], "interval": 0.1},
            "dead": {"frames": [0, 1, 2, 3, 4, 5], "interval": 0.1}
        },
        "states": {
            "patroll": enemy_states.PatrollState,
            "attack": enemy_states.AttackState,
            "dead": enemy_states.DeadState
        },
        "first_state": "patroll",
        "projectile_id": "enemy_projectile_3",
        "projectile_speed": 150,
        "score_points": 2
    },
}
