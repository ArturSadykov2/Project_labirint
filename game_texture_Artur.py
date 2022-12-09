import pygame as pg
import os
from game_texture_oleg import *

lv1_light = pg.image.load(os.path.join("levels_image", "lv1_light.png"))
lv1_traps = pg.image.load(os.path.join("levels_image", "lv1_lovyshka.png"))
ball_x = pg.image.load(os.path.join("image", "red_ball_x.png"))
ball_y = pg.image.load(os.path.join("image", "red_ball_y.png"))


texture_wood_png = pg.transform.scale(texture_wood_png, size)
bg_surface = pg.Surface(size, pg.SRCALPHA)
bg_surface.blit(texture_wood_png, (0, 0))

lv1_light = pg.transform.scale(lv1_light, size)
level_1_surf = pg.Surface(size, pg.SRCALPHA)
level_1_surf.blit(lv1_light, (0, 0))

lv1_traps = pg.transform.scale(lv1_traps, size)
level_1_traps = pg.Surface(size, pg.SRCALPHA)
level_1_traps.blit(lv1_traps, (0, 0))

ball_x = pg.transform.scale(ball_x, [size_ball, size_ball])
ball_x_surf = pg.Surface([size_ball, size_ball], pg.SRCALPHA)
ball_x_surf.blit(ball_x, (0, 0))

ball_y = pg.transform.scale(ball_y, [size_ball, size_ball])
ball_y_surf = pg.Surface([size_ball, size_ball], pg.SRCALPHA)
ball_y_surf.blit(ball_y, (0, 0))
