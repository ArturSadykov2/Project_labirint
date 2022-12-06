import pygame as pg
from random import randint
import os
from snake_colors import *

pg.init()

apfel = pg.image.load(os.path.join("image", "Food_apple.jpg"))
apfel.set_colorkey((28, 248, 18))

# load balls textures
dark_ball = pg.image.load(os.path.join("image", "dark_ball.png"))
disco_ball = pg.image.load(os.path.join("image", "disco_ball.png"))
grey_ball = pg.image.load(os.path.join("image", "grey_ball.png"))
red_ball = pg.image.load(os.path.join("image", "red_ball.png"))
striped_ball = pg.image.load(os.path.join("image", "striped_ball.png"))
magma_ball = pg.image.load(os.path.join("image", "magma_ball.png"))

go = pg.image.load(os.path.join("image", "go_down.png"))
exitt = pg.image.load(os.path.join("image", "exit_down.png"))
nextlvl = pg.image.load(os.path.join("image", "nextlvl_down.png"))
settings = pg.image.load(os.path.join("image", "settings_down.png"))

dark_down = pg.image.load(os.path.join("image", "dark_down.png"))
disco_down = pg.image.load(os.path.join("image", "disco_down.png"))
grey_down = pg.image.load(os.path.join("image", "grey_down.png"))
red_down = pg.image.load(os.path.join("image", "red_down.png"))
striped_down = pg.image.load(os.path.join("image", "striped_down.png"))
magma_down = pg.image.load(os.path.join("image", "magma_down.png"))

brick_wall = pg.image.load(os.path.join("image", "Brick_wall.png"))

screen_size = [800, 600]

screen = pg.display.set_mode(screen_size)