#The Main Game File
#import
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader
from ursinanetworking import *
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

application.development_mode = True

camera.default_shader = lit_with_shadows_shader

#The Sky
Sky(texture="sky_sunset")

#Map
Map = Entity(model="assets/models/Map.obj",
                texture="assets/textures/Map.png",
                collider="mesh",
                scale=(50, 50, 50))

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

#Pistol = Entity(model="assets/models/Pistol.obj",
#                texture="assets/textures/Pistol.png",
#                parent=camera,
#                position=(.45, -.30, .60),
#                rotation_z=.270,
#                is_reloading=False,
#                equipped=True)
Pistol = Weapon("assets/models/Pistol.obj", "assets/textures/Pistol.png", (.45, -.30, .60), False, True, .270, 0, 0)
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

#DO NOT RENAME
def update():
    if player.y <= -200:
        X, Y, Z, LV, HP, Money, Name, Volume = lib.Load("1")
        player.setPos(int(X), int(Y), int(Z))

    Save.rotation_y += 1
    Save.rotation_z += 1

    if player.intersects(Save).hit:
        Save.collider = "none"
        lib.Save("1", "0", "100", "0", str(round(player.x)), str(round(player.y)), str(round(player.z)), Volume="0.5")

#All Input functions come here
def input(key):
    CordCounter.text = f"X:{str(round(player.x))} Y:{str(round(player.y))} Z: {str(round(player.z))}"

    if key == "space" and player.grounded == False:
        player.jump()

    if held_keys["shift"]:
        player.speed = 20
    else:
        player.speed = 10

    if key == "r":
        player.set_position((0, 3, 0))

    if held_keys["f3"]:
        window.fps_counter.visible = True
        CordCounter.visible = True
    else:
        window.fps_counter.visible = False
        CordCounter.visible = False

    if key == "left mouse down":
        Pistol.Shoot(player.x, player.y, player.z, (.45, -.30, .60))

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
