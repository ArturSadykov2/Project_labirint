import pygame as pg
import math
from random import choice, randint
from game_texture_Artur import *
from game_objects import Ball


def set_level_textures(screensize, ball_size, lv1_light, mid_screen,
                       ball_texture, level_1_surface, bg_surface, ball_surface):
    level1 = pg.transform.scale(lv1_light, screensize)
    mid_screen = pg.transform.scale(mid_screen, screensize)
    bg_surface.blit(mid_screen, (0, 0))
    level_1_surface.blit(level1, (0, 0))
    ball_texture = pg.transform.scale(ball_texture, ball_size)
    ball_surface.blit(ball_texture, (0, 0))
    return level_1_surface, bg_surface, ball_surface


def draw_level(screen, level_1_surface, level_1_dang, bg_surface, ball):
    ax = int(ball.ax * 30)
    ay = int(ball.ay * 30)
    screen.blit(bg_surface, (0 - ax, 0 - ay))

    if (ax != 0) and (ay == 0):
        while ax != 0:
            screen.blit(level_1_surface, (-ax, 0))
            if ax <= 0:
                ax += 1
            else:
                ax -= 1
    elif (ax == 0) and (ay != 0):
        while ay != 0:
            screen.blit(level_1_surface, (0, -ay))
            if ay <= 0:
                ay += 1
            else:
                ay -= 1
    elif (ax != 0) and (ay != 0):
        while ax != 0:
            screen.blit(level_1_surface, (-ax, -ay))
            if ax <= 0:
                ax += 1
            else:
                ax -= 1
            if ay <= 0:
                ay += 1
            else:
                ay -= 1
    else:
        screen.blit(level_1_surface, (0, 0))
    screen.blit(level_1_dang, (0 - ax, 0 - ay))


def draw_ball(screen, ball_surface, ball):
    screen.blit(ball_surface, (ball.x, ball.y))
