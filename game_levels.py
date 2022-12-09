import pygame as pg
import math
from random import choice, randint
from game_texture_Artur import *
from game_texture_oleg import *
from game_levels_graphics import *
from game_objects import Ball
"""Вызывается из меню, сама вызывает функции отрисовки и расчета физики"""


def level(screensize, surf, walls, traps):
    screen = pg.display.set_mode(screensize)
    clock = pg.time.Clock()
    ball_surface = surf
    ball_mask = pg.mask.from_surface(ball_surface)
    level_mask = pg.mask.from_surface(walls)
    trap_mask = pg.mask.from_surface(traps)
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
        draw_level(screen, walls, traps, bg_surface, ball)
        draw_ball(screen, ball_surface, ball)
        pg.display.flip()
        clock.tick(60)
    pg.quit()
