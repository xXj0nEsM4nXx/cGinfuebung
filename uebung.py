import pgzrun
import random 

spaceship = Actor('playership2_red')
spaceship.x = 400
spaceship.y = 300
gem = Actor('gemblue')

def reset():
    if gem.y == 800:
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
        gem.x = random.randint(0, WIDTH)
        gem.y == 20

def update():
    gem.y += 2



WIDTH = 800
HEIGHT = 600


pgzrun.go()