import pygame as pg
import os
from game_texture_oleg import *

lv1_light = pg.image.load(os.path.join("levels_image", "lv1_rewalls.png"))
lv1_dark = pg.image.load(os.path.join("levels_image", "lv1_dark_2.png"))
lv1_traps = pg.image.load(os.path.join("levels_image", "lv1_lovyshki_1.png"))
ball_x = pg.image.load(os.path.join("image", "red_ball_x.png"))
ball_y = pg.image.load(os.path.join("image", "red_ball_y.png"))

texture_wood_png = pg.image.load(os.path.join("levels_image", "texture_wood.jpg"))
texture_wood_png = pg.transform.scale(texture_wood_png, size)
bg_wood_surface = pg.Surface(size, pg.SRCALPHA)
bg_wood_surface.blit(texture_wood_png, (0, 0))

texture_red_png = pg.image.load(os.path.join("levels_image", "red_background.jpg"))
texture_red_png = pg.transform.scale(texture_red_png, size)
bg_red_surface = pg.Surface(size, pg.SRCALPHA)
bg_red_surface.blit(texture_red_png, (0, 0))

lv1_light = pg.transform.scale(lv1_light, size)
lv1_walls_surf = pg.Surface(size, pg.SRCALPHA)
lv1_walls_surf.blit(lv1_light, (0, 0))

lv1_dark = pg.transform.scale(lv1_dark, size)
lv1_sp_surf = pg.Surface(size, pg.SRCALPHA)
lv1_sp_surf.blit(lv1_dark, (0, 0))

lv1_traps = pg.transform.scale(lv1_traps, size)
lv1_traps_surf = pg.Surface(size, pg.SRCALPHA)
lv1_traps_surf.blit(lv1_traps, (0, 0))

ball_x = pg.transform.scale(ball_x, [size_ball, size_ball])
ball_x_surf = pg.Surface([size_ball, size_ball], pg.SRCALPHA)
ball_x_surf.blit(ball_x, (0, 0))

ball_y = pg.transform.scale(ball_y, [size_ball, size_ball])
ball_y_surf = pg.Surface([size_ball, size_ball], pg.SRCALPHA)
ball_y_surf.blit(ball_y, (0, 0))

finish_texture = pg.image.load(os.path.join("levels_image", "final_hole.png"))
finish_texture = pg.transform.scale(finish_texture, [finish_width, finish_hight])
finish_surf = pg.Surface([finish_width, finish_hight], pg.SRCALPHA)
finish_surf.blit(finish_texture, (0, 0))

lv2_walls = pg.image.load(os.path.join("levels_image", "lv2_walls_gun.png"))
lv2_walls = pg.transform.scale(lv2_walls, size)
lv2_walls_surf = pg.Surface(size, pg.SRCALPHA)
lv2_walls_surf.blit(lv2_walls, (0, 0))
lv2_traps = pg.image.load(os.path.join("levels_image", "lv2_lovyshka.png"))
lv2_traps = pg.transform.scale(lv2_traps, size)
lv2_traps_surf = pg.Surface(size, pg.SRCALPHA)
lv2_traps_surf.blit(lv2_traps, (0, 0))

lv3_walls = pg.image.load(os.path.join("levels_image", "lv3_walls.png"))
lv3_walls = pg.transform.scale(lv3_walls, size)
lv3_walls_surf = pg.Surface(size, pg.SRCALPHA)
lv3_walls_surf.blit(lv3_walls, (0, 0))
lv3_traps = pg.image.load(os.path.join("levels_image", "lv3_lovyshka.png"))
lv3_traps = pg.transform.scale(lv3_traps, size)
lv3_traps_surf = pg.Surface(size, pg.SRCALPHA)
lv3_traps_surf.blit(lv3_traps, (0, 0))

lv4_walls = pg.image.load(os.path.join("levels_image", "lv4_walls.png"))
lv4_walls = pg.transform.scale(lv4_walls, size)
lv4_walls_surf = pg.Surface(size, pg.SRCALPHA)
lv4_walls_surf.blit(lv4_walls, (0, 0))
lv4_traps = pg.image.load(os.path.join("levels_image", "lv4_lovyshka.png"))
lv4_traps = pg.transform.scale(lv4_traps, size)
lv4_traps_surf = pg.Surface(size, pg.SRCALPHA)
lv4_traps_surf.blit(lv4_traps, (0, 0))
