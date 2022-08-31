from ursina import *
from ursina.prefabs.health_bar import HealthBar

class Zombie:
    def __init__(self):
        model="cube"
        Bar = HealthBar(text="Hi")
