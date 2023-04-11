import json

with open('config.json', 'r') as file:
    config = json.load(file)

SCREEN_WIDTH = config["screen_width"]
SCREEN_HEIGHT = config["screen_height"]
WORLD_WIDTH = config["world_width"]
WORLD_HEIGHT = config["world_height"]
