import pgzrun
import random 

spaceship = Actor('playership2_red')
spaceship.x = 400
spaceship.y = 300
gem = Actor('gemblue')
gem.x = random.randint(0,600)
gem.y = 0

def draw():
    screen.clear()
    spaceship.draw()
    gem.draw()

def on_key_down(key):
    if key == keys.RIGHT:
        spaceship.x += 30
    elif key == keys.LEFT:
        spaceship.x -= 30
    elif key == keys.UP:
        spaceship.y -= 30
    elif key == keys.DOWN:
        spaceship.y += 30

def berühren ():
   if spaceship.colliderect(gem):
        gem.x = randint(0, WIDTH)
        gem.y = randint(0,HEIGHT)

def update():
    gem.y += 5

WIDTH = 800
HEIGHT = 600

pgzrun.go()