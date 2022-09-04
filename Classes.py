from ursina import *
from ursina.prefabs.health_bar import HealthBar

class Bullet(Entity):
    def __init__(self):
        self.model = "assets/models/Bullet.obj",
        self.texture = "assets/textures/Bullet.png"
        self.collider = "mesh"

    def CreateEntity(self):
        Bullet = Entity(model=self.model,
                        texture=self.texture,
                        collider=self.collider)


        
