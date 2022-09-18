#The Main Menu for the Game
#import
import subprocess
import tkinter
from tkinter import *
import os
import sys

#Main window
root = Tk()

#window configuration
root.title("Zombie Slash")
root.iconbitmap("assets/textures/icon.ico")
root.config(bg="gray")
root.geometry("256x256")
root.resizable(width=False, height=False)

#Functions
def Quit():
    sys.exit(0)

def Start():
    subprocess.call("python Game.py")

#The Widgets of the GUI
StartButton = Button(root, text="Start", background="gray", command=Start)
StartButton.pack(pady=50)

QuitButton = Button(root, text="Quit", background="gray", command=Quit)
QuitButton.pack(pady=50)

#mainloop
root.mainloop()