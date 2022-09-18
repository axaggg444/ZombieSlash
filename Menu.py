#The Main Menu
#import
from ursina import *
import subprocess

#app
app = Ursina()

#Functions
def Quit():
    sys.exit(0)

def Start():
    subprocess.call("python Game.py")

#window configuration
window.borderless = False
window.title = "Menu"
window.icon = "assets/textures/icon.ico"
window.fps_counter.visible = False
window.exit_button.visible = False
window.center_on_screen()
window.exit_button.disable()

#Background image
img = Entity(model="cube", texture="assets/textures/icon.png", scale=(10, 10, 10), rotate_z=.45)

#Start Button
StartButton = Button(text="Start", scale=0.1, color=color.gray, y=.2)
StartButton.on_click = Start

#Quit Button
QuitButton = Button(text="Quit", scale=0.1, color=color.gray, y=-.2)
QuitButton.on_click = application.quit

#mainloop
app.run()
