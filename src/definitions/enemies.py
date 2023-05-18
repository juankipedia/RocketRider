from typing import Dict, Any

from src.states.entities import enemy_states

ENEMIES: Dict[int, Dict[str, Any]] = {
    "alan": {
        "texture_id": "alan",
        "walk_speed": 10,
        "animation_defs": {
            "idle": {"frames": [0] },
            "walk": {"frames": [0, 1, 2, 3, 4, 5], "interval": 0.1}
        },
        "states": {"patroll": enemy_states.PatrollState},
        "first_state": "patroll",
    },
    "bon_bon": {
        "texture_id": "bon_bon",
        "walk_speed": 15,
        "animation_defs": {
            "idle": {"frames": [0] },
            "walk": {"frames": [0, 1, 2, 3], "interval": 0.15}
        },
        "states": {"patroll": enemy_states.PatrollState},
        "first_state": "patroll",
    },
    "lips": {
        "texture_id": "lips",
        "walk_speed": 10,
        "animation_defs": {
            "idle": {"frames": [0] },
            "walk": {"frames": [0, 1, 2, 3, 4], "interval": 0.1}
        },
        "states": {"patroll": enemy_states.PatrollState},
        "first_state": "patroll",
    }
}
