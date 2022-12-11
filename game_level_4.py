import pygame as pg
import math
from random import choice, randint
from game_texture_Artur import *
from game_texture_oleg import *
from game_levels_graphics import *
from game_objects_ball import Ball
from game_object_gun import Bullet


def level_4(screensize, ball_surf, menu):
    x4 = 100
    y4 = 360
    xf4 = 1200
    yf4 = 360
    screen = pg.display.set_mode(screensize)
    clock = pg.time.Clock()
    ball_surface = ball_surf
    ball_mask = pg.mask.from_surface(ball_surface)
    level_mask = pg.mask.from_surface(lv4_walls_surf)
    trap_mask = pg.mask.from_surface(lv4_traps_surf)
    ball_x_mask = pg.mask.from_surface(ball_x_surf)
    ball_y_mask = pg.mask.from_surface(ball_y_surf)
    finish_mask = pg.mask.from_surface(finish_surf)
    running = True
    ball = Ball(x4, y4)
    ball.__init__(x4, y4)
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        ball.ball_boost()
        Ball.ball_move(ball)
        Ball.collusion(ball, level_mask, ball_mask, trap_mask, ball_x_mask, ball_y_mask, x4, y4)
        draw_level(screen, lv4_walls_surf, lv4_traps_surf, bg_wood_surface, ball, finish_surf, xf4, yf4, lv4_dark_surf)
        draw_ball(screen, ball_surface, ball)
        running = ball.finish(ball_mask, finish_mask, menu, xf4, yf4, running)
        pg.display.flip()
        clock.tick(60)
