#The Main Game File
#import
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

#Ask the user for the Server and Port
#IP = input("Enter IP Address:")
#PORT = input("Enter PORT:")
#Username = input("Enter Username:")

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
X, Y, Z, LV, HP, Money, Name = lib.Load("1")
player.setPos(int(X), int(Y), int(Z))

#Lightning
pivot = Entity()
AmbientLight(parent=pivot, y=10, z=3, shadows=True)

#Map
ground = Entity(model="plane", texture="grass", color=color.green, scale=(100, 1, 100), collider="mesh")

SaveBeam = Entity(model="cube", scale=(1, 100, 1), y=-50, color=color.yellow, collider="mesh", position=(40, 0, 40))

StupidHouse = Entity(model="assets/models/StupidHouse.obj", texture="assets/textures/StupidHouse.png", scale=(30, 30, 30), collider="mesh", shader=lit_with_shadows_shader)

#DO NOT RENAME
def update():
    if player.y <= -200:
        X, Y, Z, LV, HP, Money, Name = lib.Load("1")
        player.setPos(int(X), int(Y), int(Z))

    SaveBeam.rotation_y += 1

    if player.intersects(SaveBeam).hit:
        SaveBeam.collider = "none"
        lib.Save("1", "0", "100", "0", str(round(player.x)), str(round(player.y)), str(round(player.z)))

def input(key):
    if held_keys["shift"]:
        player.speed = 20
    else:
        player.speed = 10

    if key == "escape":
        sys.exit(0)

#mainloop
app.run()
