import pygame as pg
import math
from random import choice, randint
from game_texture_Artur import *
from game_texture_oleg import *
from game_levels_graphics import *
from game_objects import Ball
"""Вызывается из меню, сама вызывает функции отрисовки и расчета физики"""


def level(screensize, surf, walls, traps, x, y, x_finish, y_finish, menu):
    screen = pg.display.set_mode(screensize)
    clock = pg.time.Clock()
    ball_surface = surf
    ball_mask = pg.mask.from_surface(ball_surface)
    level_mask = pg.mask.from_surface(walls)
    trap_mask = pg.mask.from_surface(traps)
    ball_x_mask = pg.mask.from_surface(ball_x_surf)
    ball_y_mask = pg.mask.from_surface(ball_y_surf)
    finish_mask = pg.mask.from_surface(finish_surf)
    running = True
    ball = Ball(x, y)
    ball.__init__(x, y)
    while running:
        Ball.ball_boost(ball)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        Ball.ball_move(ball)
        Ball.collusion(ball, level_mask, ball_mask, trap_mask, ball_x_mask, ball_y_mask, x, y)
        draw_level(screen, walls, traps, bg_surface, ball, finish_surf, x_finish, y_finish)
        draw_ball(screen, ball_surface, ball)
        running = ball.finish(ball_mask, finish_mask, menu, x_finish, y_finish, running)
        pg.display.flip()
        clock.tick(60)
        print(running)
