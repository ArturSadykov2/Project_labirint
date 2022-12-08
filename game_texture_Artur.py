import pygame as pg
import os
from game_texture_oleg import *

lv1_light = pg.image.load(os.path.join("levels_image", "lv1_light.png"))
lv1_lov = pg.image.load(os.path.join("levels_image", "lv1_lovyshka.png"))

texture_wood_png = pg.transform.scale(texture_wood_png, size)
bg_surface = pg.Surface(size, pg.SRCALPHA)
bg_surface.blit(texture_wood_png, (0, 0))

lv1_light = pg.transform.scale(lv1_light, size)
level_1_surf = pg.Surface(size, pg.SRCALPHA)
level_1_surf.blit(lv1_light, (0, 0))

lv1_lov = pg.transform.scale(lv1_lov, size)
level_1_dang = pg.Surface(size, pg.SRCALPHA)
level_1_dang.blit(lv1_lov, (0, 0))
