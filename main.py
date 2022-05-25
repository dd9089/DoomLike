from ursina import *

app = Ursina()

cube = Entity (modle = 'cube', color = color.orange, scale = (2, 2, 2))
cube.update()
app.run()


def update():
    cube.rotation_y += time.dt * 100