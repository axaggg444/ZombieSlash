from ursina import *
from ursina.prefabs.health_bar import HealthBar

class Bullet(Entity):
    def __init__(pos, speed = 2000):
        super().__init__(
            model = "assets/models/Bullet.obj",
            texture = "assets/textures/Bullet.png",
            collider = "mesh",
            scale = 0.08,
            position = pos)


        
