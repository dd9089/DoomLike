from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
window.fullscreen = True

player = FirstPersonController()
player.position = (0, 1, 0)
ground = Entity (model = 'plane', color = color.red, texture = "grass", scale = 100, position = (0, 0, 0), collider = 'box')
wall = [
    Entity(model='cube', color=color.white, texture='cobblestone', scale=(100, 20, 0.0005), position=(0, 5, 50), collider='box'),
    Entity(model='cube', color=color.white, texture='cobblestone', scale=(100, 20, 0.0005), position=(0, 5, -50), collider='box'),
    Entity(model='cube', color=color.white, texture='cobblestone', scale=(0.0005, 20, 100), position=(-50, 5, 0), collider='box'),
    Entity(model='cube', color=color.white, texture='cobblestone', scale=(0.0005, 20, 100), position= (50, 5, 0), collider='box')
    ]

leg = Entity(model='cube', color=color.green, position = (0, 0.5, 0), collider='box', )


def update():
    if held_keys['escape']:
        quit()

    if held_keys['r'] and leg.visible == True:
        leg.visible = False
    elif held_keys['r']:
        leg.visible = True
    if held_keys['e']:
        destroy(leg)
   # leg.z += held_keys['w'] * .08


def on_click(self):
    destroy(self)




app.run()
