from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
window.fullscreen = True
window.exit_button.enabled = False
mouse.visible = False
Sky(texture='sky')


class Demon:
    def __init__(self, health, speed, damage):
        self.demon = Entity(model='sphere', color=color.white, texture='deamon', scale=10, position=(2, 10, 20), collider='sphere')
        self.health = health
        self.speed = speed
        self.damage = damage
        self.demon.look_at(player)

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
        self.slayer = Entity(model='sphere', color=color.green, position=player.position, scale=(0.5, 0.5, 1.5))
        self.hp = 100
        self.ammo = 0
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
        '''if (crosshairs over demon):
            demonHealth = demonHealth - 20
        if (demonHealth = 0 or demonHealth < 0):
            remove
            demon
            entity'''

    def move(self):
        self.slayer.position = (player.x + 0.3, player.y + 2.5, player.z + 0.3)
        #self.slayer.look_at(mouse.point)



class Demon2:

    def __init__(self, health, speed, damage):
        self.demon = Entity(model='rectangle', color=color.white, texture = 'deamon', scale = (2, 4, 2), position = (2, 10, 20), collider = 'rectangle')
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

    def notice(self):
       if distance(self.demon.position, player.position) >= 30:
           self.aggro()

    def attack(self):
        count = 0

        if distance(self.demon.position, player.position) <= 10:
            while count < 15:
                if player.x > self.demon.x and distance(self.demon.position, player.position) > 2:
                    self.fireBall.x += .05
                    count += 1
                if player.x < self.demon.x and distance(self.demon.position, player.position) > 2:
                    self.fireBall.x -= .05
                    count += 1
        elif distance(self.demon.position, player.position) <= 1:
           #player.setHealth(player.getHealth() - self.damage)
               pass

    def die(self):
       destroy(self.demon)


class Projectile:

    def __init__(self, pos):
        self.projectile = Entity(model='sphere', color=color.orange, scale=1, position=pos)
        self.fire()

    def fire(self):
        self.projectile.look_at(player)
        self.projectile.speed = 30
        if self.projectile.distance(player) < .5:
            # player.setHealth(player.health - 5)
            destroy(self.projectile)
        destroy(self.projectile, delay=3)


player = FirstPersonController()
player.position = (0, 0, 0)
player.scale = 1.5
player.jump_height = 4

demon = Demon(10, 5, 2)
slayer = Slayer()

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
        slayer.move()
    except:
        pass


app.run()