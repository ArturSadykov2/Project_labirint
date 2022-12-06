import pygame as pg
import math
from random import choice, randint


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
size = [1600, 900]


screen = pg.display.set_mode(size)
clock = pg.time.Clock()
level_texture = pg.image.load('mask_lv2_without_background.png').convert_alpha()
bg_texture = pg.image.load('bg_texture.jpg').convert_alpha()
bg_texture = pg.transform.scale(bg_texture, size)
level_texture = pg.transform.scale(level_texture, size)
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

    screen.fill((255, 255, 255))
    screen.blit(bg_surface, (0, 0))
    screen.blit(labirint_surface, (0, 0))
    pg.display.flip()
    clock.tick(60)
pg.quit()
