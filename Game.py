#The Main Game File
#import
from turtle import position
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader
from ursina.prefabs.health_bar import HealthBar
import Classes
import sys
import lib
import socket

#The Socket
Client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

app = Ursina()

#Window Config
window.fullscreen = True
window.exit_button.visible = False
window.title = "Game"
window.icon = "assets/textures/icon.ico"

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
                is_reloading=False)

#DO NOT RENAME
def update():
    if player.y <= -200:
        X, Y, Z, LV, HP, Money, Name = lib.Load("1")
        player.setPos(int(X), int(Y), int(Z))

    Save.rotation_y += 1
    Save.rotation_z += 1

    if player.intersects(Save).hit:
        Save.collider = "none"
        lib.Save("1", "0", "100", "0", str(round(player.x)), str(round(player.y)), str(round(player.z)), Volume=Volume)

#All Input functions come here
def input(key):
    if held_keys["shift"]:
        player.speed = 20
    else:
        player.speed = 10

    if key == "left_mouse_down" and Pistol.is_reloading == False:
        Bullet = Classes.Bullet()
        Bullet.CreateEntity()

    if key == "escape":
        sys.exit(0)

#mainloop
app.run()
