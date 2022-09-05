#The Main Game File
#import
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader
from ursina.prefabs.health_bar import HealthBar
import Classes
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

Entity.default_shader = lit_with_shadows_shader

#The Sky
Sky(texture="sky_sunset")

#The Player
player = FirstPersonController(collider="box")
player.setPos(0, 111, 0)

player.cursor.color = color.black

#Load the Game
X, Y, Z, LV, HP, Money, Name, Volume = lib.Load("1")
player.setPos(int(X), int(Y), int(Z))

#Lightning
pivot = Entity()
AmbientLight(parent=pivot, y=10, z=3, shadows=True)

#Player Health bar
Bar = HealthBar(bar_color=color.gray, 
                show_text=True, 
                max_value=100, 
                roundness=.07,
                x=-.1)

#Coordinate Counter
CordCounter = Text(text=f"X:{str(round(player.x))} Y:{str(round(player.y))} Z: {str(round(player.z))}", y=.1, x=-.1, color=color.dark_gray)
CordCounter.visible = False

#Background Music
Music = Audio(sound_file_name="assets/sound/Background.mp3", 
                autoplay=True, 
                loop=True, 
                volume=0.5)

#Map
ground = Entity(model="plane", 
                texture="grass", 
                color=color.green, 
                scale=(100, 1, 100), 
                collider="mesh")

Save = Entity(model="assets/models/Save.obj", 
                    scale=(2, 2, 2), 
                    texture="assets/textures/Save.png", 
                    collider="mesh", 
                    position=(40, 2, 40))

StupidHouse = Entity(model="assets/models/StupidHouse.obj", 
                        texture="assets/textures/StupidHouse.png", 
                        scale=(30, 30, 30), 
                        collider="mesh", 
                        shader=lit_with_shadows_shader)

Jeff = Entity(model="assets/models/Jeff.obj",
                texture="assets/textures/Jeff.png",
                position=(2, 0 , 2),
                scale=(1.5, 1.5, 1.5),
                collider="mesh")

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

    if held_keys["shift"]:
        player.speed = 20
    else:
        player.speed = 10

    if key == "left_mouse_down" and Pistol.is_reloading == False:
        Bullet = Classes.Bullet(pos=(player.x, player.y, player.z))

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
