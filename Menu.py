from ursina import *
import subprocess

app = Ursina()

def Quit():
    sys.exit(0)

def Start():
    subprocess.call("python Game.py")

window.borderless = False
window.title = "Menu"
window.icon = "assets/textures/icon.ico"
window.fps_counter.visible = False
window.exit_button.visible = False
img = Entity(model="cube", texture="assets/textures/icon.png", scale=(10, 10, 10), rotate_z=.45)

#Start Button
StartButton = Button(text="Start", scale=0.1, color=color.gray, y=.2)
#Change
StartButton.on_click = Start

#Quit Button
#Works fine
QuitButton = Button(text="Quit", scale=0.1, color=color.gray, y=-.2)
QuitButton.on_click = application.quit
app.run()