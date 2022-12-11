import pygame as pg
import math
from random import choice, randint
from game_texture_Artur import *
from game_texture_oleg import *
from game_levels_graphics import *
from game_objects_ball import Ball


def level_1(screensize, ball_surf, menu):
    x1 = 80
    y1 = 500
    xf1 = 80
    yf1 = 600
    screen = pg.display.set_mode(screensize)
    clock = pg.time.Clock()
    ball_surface = ball_surf
    ball_mask = pg.mask.from_surface(ball_surface)
    level_mask = pg.mask.from_surface(lv1_walls_surf)
    trap_mask = pg.mask.from_surface(lv1_traps_surf)
    ball_x_mask = pg.mask.from_surface(ball_x_surf)
    ball_y_mask = pg.mask.from_surface(ball_y_surf)
    finish_mask = pg.mask.from_surface(finish_surf)
    running = True
    ball = Ball(x1, y1)
    ball.__init__(x1, y1)
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        ball.ball_boost()
        Ball.ball_move(ball)
        Ball.collusion(ball, level_mask, ball_mask, trap_mask, ball_x_mask, ball_y_mask, x1, y1)
        draw_level(screen, lv1_walls_surf, lv1_traps_surf, bg_wood_surface, ball, finish_surf, xf1, yf1, lv1_dark_surf)
        draw_ball(screen, ball_surface, ball)
        running = ball.finish(ball_mask, finish_mask, menu, xf1, yf1, running)
        pg.display.flip()
        clock.tick(60)
