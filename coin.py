#!/Library/Frameworks/Python.framework/Versions/3.11/bin/pgzrun
import pgzrun
from pygame import *
from random import *
WIDTH = 600
HEIGHT = 600
score = 0
game_over = False
fox = Actor("fox")
fox.pos = 200, 200
coin = Actor("coin")
coin.pos = 200, 200

def draw():
    screen.fill("green")
    fox.draw()
    coin.draw()
    screen.draw.text(f"Score: {str(score)}", color="black", topleft=(10, 10))

    if game_over == True:
        screen.fill("pink")
        screen.draw.text(f"Score: {str(score)}", topleft=(10, 10), fontsize=60)

def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT -20))

def time_up():
    global game_over
    game_over = True

def update():
    global score

    if keyboard.left:
        fox.x = fox.x - 5
    elif keyboard.right:
        fox.x = fox.x + 5
    elif keyboard.up:
        fox.y = fox.y - 5
    elif keyboard.down:
        fox.y = fox.y + 5
    
    coin_collected = fox.colliderect(coin)

    if coin_collected:
        score += 10
        place_coin()

clock.schedule(time_up, 16.0)
place_coin()
pgzrun.go()