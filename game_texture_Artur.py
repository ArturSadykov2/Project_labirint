import pygame as pg
import os
from game_texture_oleg import *

lv1_light = pg.image.load(os.path.join("levels_image", "lv1_light.png"))


bg = pg.transform.scale(home_screen_png, size)
home_surface = pg.Surface(size, pg.SRCALPHA)
home_surface.blit(home, (0, 0))

home = pg.transform.scale(home_screen_png, size)
home_surface = pg.Surface(size, pg.SRCALPHA)
home_surface.blit(home, (0, 0))

home = pg.transform.scale(home_screen_png, size)
home_surface = pg.Surface(size, pg.SRCALPHA)
home_surface.blit(home, (0, 0))
