import pygame as pg
import math
from random import choice, randint
from game_texture_Artur import *
from game_texture_oleg import *
from game_levels_graphics import *
from game_objects import Ball
"""Вызывается из меню, сама вызывает функции отрисовки и расчета физики"""


def level_1(screensize, ball_size, ball_texture):
    screen = pg.display.set_mode(screensize)
    clock = pg.time.Clock()
    bg_surface = pg.Surface(screensize, pg.SRCALPHA)
    level_1_surface = pg.Surface(screensize, pg.SRCALPHA)
    ball_surface = pg.Surface(screensize, pg.SRCALPHA)
    set_level_textures(screensize, ball_size, lv1_light, mid_screen, ball_texture, level_1_surface, bg_surface, ball_surface)
    ball_mask = pg.mask.from_surface(ball_surface)
    level_mask = pg.mask.from_surface(level_1_surface)
    running = True
    ball = Ball(ball_texture)
    ball.__init__(ball_texture)
    while running:
        Ball.ball_boost(ball)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        Ball.ball_move(ball)
        masks(level_mask, ball_mask)
        draw_level(screen, level_1_surface, bg_surface, ball)
        draw_ball(screen, ball_surface, ball)
        pg.display.flip()
        clock.tick(60)
    pg.quit()


level_1([1392, 783], [60, 60], disco_ball_png)

