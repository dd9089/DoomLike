from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
window.fullscreen = True
Sky(texture='sky')


class Demon:
    def __init__(self, health, speed, damage):
        self.demon = Entity(model='sphere', color=color.white, texture='deamon', scale=10, position=(2, 10, 20),
                            collider='sphere')
        self.health = health
        self.speed = speed
        self.damage = damage

    def aggro(self):
        if player.x > self.demon.x and distance(self.demon.position, player.position) > 2:
            self.demon.x += .05
        if player.x < self.demon.x and distance(self.demon.position, player.position) > 2:
            self.demon.x -= .05
        if player.z > self.demon.z and distance(self.demon.position, player.position) > 2:
            self.demon.z += .05
        if player.z < self.demon.z and distance(self.demon.position, player.position) > 2:
            self.demon.z -= .05
        self.demon.look_at(player)

    def notice(self):
        if distance(self.demon.position, player.position) >= 30:
            self.aggro()

    def attack(self):
        if distance(self.demon.position, player.position) <= 1:
            # player.setHealth(player.getHealth() - self.damage)
            pass

    def die(self):
        destroy(self.demon)


class Slayer:
    def __init__(self):
        self.hp = 100
        self.ammo = 0
        self.x = 0
        self.y = 0
        self.z = 0
        self.shoot = True

    def get_health(self):
        return self.hp

    def set_health(self, h):
        self.hp = h
        return self.hp

    def get_ammo(self):
        return self.ammo

    def set_ammo(self, a):
        self.ammo = a
        return self.ammo

    def shoot(self):
        self.ammo = self.ammo - 1
        '''if ():#crosshairs over demon):
            demonHealth = demonHealth - 20
        if (demonHealth = 0 or demonHealth < 0):
            remove
            demon
            entity'''


player = FirstPersonController()
player.position = (0, 0, 0)
player.scale = 1.5
player.jump_height = 4

demon = Demon(10, 5, 2)

ground = Entity(model='plane', color=color.red, texture="grass", scale=100, position=(0, 0, 0), collider='mesh')
wall = [
    Entity(model='cube', color=color.white, texture='cobblestone', scale=(100, 20, 0.0005), position=(0, 5, 50),
           collider='mesh'),
    Entity(model='cube', color=color.white, texture='cobblestone', scale=(100, 20, 0.0005), position=(0, 5, -50),
           collider='mesh'),
    Entity(model='cube', color=color.white, texture='cobblestone', scale=(0.0005, 20, 100), position=(-50, 5, 0),
           collider='mesh'),
    Entity(model='cube', color=color.white, texture='cobblestone', scale=(0.0005, 20, 100), position=(50, 5, 0),
           collider='mesh')
]


def update():
    if held_keys['escape']:
        quit()
    if held_keys['shift']:
        player.speed = 15
    else:
        player.speed = 10
    if held_keys['e']:
        demon.die()
    try:
        demon.notice()
        demon.attack()
    except:
        pass


app.run()