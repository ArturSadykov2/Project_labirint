import pygame as pg
import math
from random import choice, randint
from game_texture_Artur import *
from game_texture_oleg import *
from game_levels_graphics import *
from game_objects import Ball
"""Вызывается из меню, сама вызывает функции отрисовки и расчета физики"""


def level_1(screensize, surf):
    screen = pg.display.set_mode(screensize)
    clock = pg.time.Clock()
    ball_surface = surf
    ball_mask = pg.mask.from_surface(ball_surface)
    level_mask = pg.mask.from_surface(lv1_walls_surf)
    trap_mask = pg.mask.from_surface(lv1_traps_surf)
    ball_x_mask = pg.mask.from_surface(ball_x_surf)
    ball_y_mask = pg.mask.from_surface(ball_y_surf)
    running = True
    x = 100
    y = 100
    ball = Ball(x, y)
    ball.__init__(x, y)
    while running:
        Ball.ball_boost(ball)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        Ball.ball_move(ball)
        Ball.collusion(ball, level_mask, ball_mask, trap_mask, ball_x_mask, ball_y_mask)
        draw_level(screen, lv1_walls_surf, lv1_traps_surf, bg_surface, ball)
        draw_ball(screen, ball_surface, ball)
        pg.display.flip()
        clock.tick(60)
    pg.quit()


#level_1([1392, 783], [60, 60], disco_ball_png)

