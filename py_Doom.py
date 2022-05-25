from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
window.fullscreen = True

player = FirstPersonController()
player.position = (0, 0, 0)
player.scale = 1.5

ground = Entity (model = 'plane', color = color.red, texture = "grass", scale = 100, position = (0, 0, 0), collider = 'mesh')
wall = [
    Entity(model='cube', color=color.white, texture='cobblestone', scale=(100, 20, 0.0005), position=(0, 5, 50), collider='mesh'),
    Entity(model='cube', color=color.white, texture='cobblestone', scale=(100, 20, 0.0005), position=(0, 5, -50), collider='mesh'),
    Entity(model='cube', color=color.white, texture='cobblestone', scale=(0.0005, 20, 100), position=(-50, 5, 0), collider='mesh'),
    Entity(model='cube', color=color.white, texture='cobblestone', scale=(0.0005, 20, 100), position= (50, 5, 0), collider='mesh')
    ]


def update():
    if held_keys['escape']:
        quit()
    if held_keys['shift']:
        player.speed = 15
    else:
        player.speed = 10


def on_click(self):
    destroy(self)




app.run()
