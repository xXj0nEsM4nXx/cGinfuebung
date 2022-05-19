import pgzrun
import random

spaceship = Actor('playership1_red')
gem = Actor('gemblue')

def draw():
    screen.clear()
    spaceship.draw()
    gem.draw()

def on_key_down(key):
    if key == keys.RIGHT:
        spaceship.x = +30
    elif key == keys.LEFT:
        spaceship.x = -30
    elif key == keys.UP:
        spaceship.y = +30
    elif key == keys.DOWN:
        spaceship.y = -30

WIDTH = 800
HEIGHT = 600


pgzrun.go()