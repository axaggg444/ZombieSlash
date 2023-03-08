from ursina import *

class Bullet(Entity):
    def __init__(self, add_to_scene_entities=True, **kwargs):
        super().__init__(add_to_scene_entities, **kwargs,
        model="assets/models/Bullet.obj",
        texture="assets/textures/Bullet.png")

class Weapon(Entity):
    def __init__(self, model, texture, ui_pos, is_reloading, equipped, rotation_y, rotation_z, rotation_x,):
        super().__init__(
        parent=camera,
        model=model,
        texture=texture,
        position=ui_pos,
        is_reloading=is_reloading,
        equipped=equipped,
        rotation_x=rotation_x,
        rotation_y=rotation_y,
        rotation_z=rotation_z)

    def Shoot(self, playerx, playery, playerz, ui_pos):
        Bullet1 = Bullet()
        Bullet1.setPos(ui_pos)
        #Bullet1.setPos((playerx, playery, playerz))

