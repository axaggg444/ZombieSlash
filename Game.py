#The Main Game File
#import
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader
from ursina.prefabs.health_bar import HealthBar
from ursina.mesh_importer import obj_to_ursinamesh
from Classes import *
import sys
import lib

#Application Creation
app = Ursina()

#Window Config
window.fullscreen = True
window.exit_button.visible = False
window.title = "Game"
window.icon = "assets/textures/icon.ico"
window.fps_counter.visible = False

application.development_mode = False

lit_with_shadows_shader.compile()

Entity.default_shader = lit_with_shadows_shader

#The Sky
Sky(texture="sky_sunset")

#Map
Map = Entity(model="assets/models/Map.obj",
                texture="assets/textures/Map.png",
                collider="mesh",
                scale=(50, 50, 50))

def TeleportTo1():
    player.setPos((-20, 20, -60))

def TeleportTo2():
    player.setPos((-20, 30, 100))


#The Player
player = FirstPersonController(collider="box")
player.setPos(0, 0, 0)

player.cursor.color = color.black

Bullet1 = Bullet()

#Load the Game
X, Y, Z, LV, HP, Money, Name, Volume = lib.Load("1")
player.setPos(int(X), int(Y), int(Z))

#Lightning
pivot = Entity()
AmbientLight(parent=pivot, y=10, z=3, shadows=True)

#Coordinate Counter
CordCounter = Text(text=f"X:{str(round(player.x))} Y:{str(round(player.y))} Z: {str(round(player.z))}", y=.1, x=-.1, color=color.dark_gray)
CordCounter.visible = False

#Background Music
Music = Audio(sound_file_name="assets/sound/Background.mp3",
                autoplay=True,
                loop=True,
                volume=0.5)

#Map
Save = Entity(model="assets/models/Save.obj",
                    scale=(2, 2, 2),
                    texture="assets/textures/Save.png",
                    collider="mesh",
                    position=(10, 4, 5))

Pistol = Entity(model="assets/models/Pistol.obj",
                texture="assets/textures/Pistol.png",
                parent=camera,
                position=(.45, -.30, .60),
                rotation_z=.270,
                is_reloading=False,
                equipped=True)

Rifle = Entity(model="assets/models/Rifle.obj",
                texture="assets/textures/Rifle.png",
                parent=scene,
                position=(.45, -.30, .60),
                rotation_z=.270,
                is_reloading=False,
                equipped=False)

Zombie = Entity(model="assets/models/Zombie.obj",
                texture="assets/textures/Zombie.png",
                collider="mesh",
                scale=10)

#The Jump pads
Pad1 = Entity(model="cube",
                color=color.red,
                collider="mesh",
                scale=(5, 1, 5),
                position=(-13, 3, -21))

Pad2 = Entity(model="cube",
                color=color.red,
                collider="mesh",
                scale=(5, 1, 5),
                position=(-13, 3, 21))

#DO NOT RENAME
def update():
    if player.y <= -200:
        X, Y, Z, LV, HP, Money, Name, Volume = lib.Load("1")
        player.setPos(int(X), int(Y), int(Z))

#    for i in Zombies:
#        i.look_at(player)
#        i.position += i.forward

    Save.rotation_y += 1
    Save.rotation_z += 1

    if player.intersects(Save).hit:
        Save.collider = "none"
        lib.Save("1", "0", "100", "0", str(round(player.x)), str(round(player.y)), str(round(player.z)), Volume="0.5")

    if player.intersects(Pad1).hit:
        TeleportTo1()

    if player.intersects(Pad2).hit:
        TeleportTo2()

#All Input functions come here
def input(key):
    CordCounter.text = f"X:{str(round(player.x))} Y:{str(round(player.y))} Z: {str(round(player.z))}"

    if key == "space" and player.grounded == False:
        player.jump()

    if held_keys["shift"]:
        player.speed = 20
    else:
        player.speed = 10

    if key == "left_mouse_down":
        if player.look_at(Entity):
            print("Hi")

    if key == "r":
        player.set_position((0, 3, 0))

    if held_keys["f3"]:
        window.fps_counter.visible = True
        CordCounter.visible = True
    else:
        window.fps_counter.visible = False
        CordCounter.visible = False

    if key == "1":
        Pistol.parent = camera
        Rifle.parent = scene

    if key == "2":
        Pistol.parent = scene
        Rifle.parent = camera

    if key == "escape":
        sys.exit(0)

#mainloop
app.run()
