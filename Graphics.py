import pygame as pg
import math
from random import choice, randint
from game_texture import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
size = [1600, 900]


def set_level_textures(screensize, level1, mid_screen):
   level1 = pg.transform.scale(level1, screensize)
   mid_screen = pg.transform.scale(mid_screen, screensize)
   bg_surface = pg.Surface(screensize, pg.SRCALPHA)
   bg_surface.blit(mid_screen, (0, 0))
   level1_surface = pg.Surface(screensize, pg.SRCALPHA)
   level1_surface.blit(level1, (0, 0))
   return level1_surface, bg_surface


screen = pg.display.set_mode(size)
clock = pg.time.Clock()
ball = pg.image.load('ball.png')#.convert_alpha()
level_texture = pg.image.load('mask_lv2_without_background.png')#.convert_alpha()
bg_texture = pg.image.load('bg_texture.jpg')#.convert_alpha()
bg_texture = pg.transform.scale(bg_texture, size)
level_texture = pg.transform.scale(level_texture, size)
ball = pg.transform.scale(ball, (50, 50))
bg_surface = pg.Surface(size, pg.SRCALPHA)
bg_surface.blit(bg_texture, (0, 0))
labirint_surface = pg.Surface(size, pg.SRCALPHA)
labirint_surface.blit(level_texture, (0, 0))
labirint_mask = pg.mask.from_surface(labirint_surface)


running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                running = False

    screen.blit(bg_surface, (0, 0))
    screen.blit(labirint_surface, (8, 8))
    screen.blit(labirint_surface, (6, 6))
    screen.blit(labirint_surface, (4, 4))
    screen.blit(labirint_surface, (2, 2))
    screen.blit(labirint_surface, (0, 0))
    screen.blit(ball, (150, 150))
    pg.display.flip()
    clock.tick(60)
pg.quit()
