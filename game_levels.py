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
    #a = 1
    while running:
        print(0)
        ball.ball_boost()
        print(1)
        Ball.ball_move(ball)
        print(2)
        Ball.collusion(ball, level_mask, ball_mask, trap_mask, ball_x_mask, ball_y_mask, x, y)
        print(3)
        draw_level(screen, walls, traps, bg_wood_surface, ball, finish_surf, x_finish, y_finish)
        print(4)
        draw_ball(screen, ball_surface, ball)
        print(5)
        running = ball.finish(ball_mask, finish_mask, menu, x_finish, y_finish, running)
        print(6)
        pg.display.flip()
        print(7)
        clock.tick(60)
        print(8)
