from ursina import *

class Bullet(Entity):
    def __init__(self, add_to_scene_entities=True, **kwargs):
        super().__init__(add_to_scene_entities, **kwargs,
        model="./assets/models/Bullet.obj",
        texture="./assets/textures/Bullet.png")

