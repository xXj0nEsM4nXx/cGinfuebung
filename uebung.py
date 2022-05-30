import pgzrun
import random 


score = 0
spaceship = Actor('playership2_red')
spaceship.x = 400
spaceship.y = 300
gem = Actor('gemblue')
gem.x = random.randint(0,600)
gem.y = 0

def reset():
    global score
    if gem.y == 800:
        gem.y = 0 
        score -= 10



def draw():
    screen.clear()
    spaceship.draw()
    gem.draw()
    screen.draw.text("score: " + str (score),(10, 10))
    


    


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
    global score
    if spaceship.colliderect(gem):
        gem.x = random.randint(0, WIDTH)
        gem.y = 20
        score += 10


def update():
    gem.y += 2
    berühren()
    reset()

WIDTH = 800
HEIGHT = 600

pgzrun.go()