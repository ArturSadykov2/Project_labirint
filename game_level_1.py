import pygame as pg
import math
from random import choice, randint
from game_texture_Artur import *
from game_texture_oleg import *
from game_levels_graphics import *
from game_objects_ball import Ball


def level(screensize, ball_surf, walls, traps, lv_dark, x, y, x_finish, y_finish, menu):
    screen = pg.display.set_mode(screensize)
    clock = pg.time.Clock()
    ball_surface = ball_surf
    ball_mask = pg.mask.from_surface(ball_surface)
    level_mask = pg.mask.from_surface(walls)
    trap_mask = pg.mask.from_surface(traps)
    ball_x_mask = pg.mask.from_surface(ball_x_surf)
    ball_y_mask = pg.mask.from_surface(ball_y_surf)
    finish_mask = pg.mask.from_surface(finish_surf)
    bullet_mask = pg.mask.from_surface(dark_ball_surface)
    running = True
    ball = Ball(x, y)
    ball.__init__(x, y)
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        ball.ball_boost()
        Ball.ball_move(ball)
        Ball.collusion(ball, level_mask, ball_mask, trap_mask, ball_x_mask, ball_y_mask, x, y, bullet_mask)
        draw_level(screen, walls, traps, bg_wood_surface, ball, finish_surf, x_finish, y_finish, lv_dark)
        draw_ball(screen, ball_surface, ball)
        running = ball.finish(ball_mask, finish_mask, menu, x_finish, y_finish, running)
        pg.display.flip()
        clock.tick(60)
