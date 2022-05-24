from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

window.fullscreen = True
window.exit_button.enabled = False
window.borderless = True
block = []

player = Entity(model='sphere', color=color.white, texture="rainbow", scale=2)
player2 = FirstPersonController()

class Voxel(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = .5,
            texture = 'white_cube',
            color = color.color(0, 0, random.uniform(.9, 1.0)),
            highlight_color = color.lime,
        )


def load_chunk(block, posX, posZ):
    for z in range(8):
        for x in range(8):
            block.append(Voxel(position=(x + posX, 0, z + posZ)))


load_chunk(block, 0, 0)
load_chunk(block, -8, 0)
load_chunk(block, 0, 8)


def update():
    see_f = raycast(player2.position + (0, 0, 8), (0, 0, 8), distance=1)
    see_l = raycast(player2.position + (-8, 0, 0), (-8, 0, 0), distance=1)
    see_r = raycast(camera.world_position + (8, 0, 0), (8, 0, 0), distance=1)
    see_b = raycast(player2.position + (0, 0, -8), (0, 0, -8), distance=1)

    if not see_l.hit:
        load_chunk(block, player2.x - 8, player2.z)
    if not see_r.hit:
        load_chunk(block, player2.x + 8, player2.z)
    if not see_f.hit:
        load_chunk(block, player2.x, player2.z + 8)
    if not see_b.hit:
        load_chunk(block, player2.x, player2.z - 8)

    #print(player2.x, player2.z, "hello")

    try:
        player.rotation_y += held_keys['left arrow']
        player.rotation_y -= held_keys['right arrow']
        player.rotation_x += held_keys['down arrow']
        player.rotation_x -= held_keys['up arrow']

        player.y -= held_keys['k'] * .05
        player.y += held_keys['i'] * .05
        player.x -= held_keys['l'] * .05
        player.x += held_keys['j'] * .05
        player.z -= held_keys['u'] * .05
        player.z += held_keys['o'] * .05
    except:
        pass

    if held_keys['escape']:
        quit()


app.run()
