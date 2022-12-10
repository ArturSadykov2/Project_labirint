import pygame as pg
import math
from random import choice, randint
from game_texture_Artur import *
from game_objects import Ball


def draw_level(screen, level_1_surface, level_1_dang, bg_surface, ball, finish, x_finish, y_finish):
    ax = 10
    ay = 10
    screen.blit(bg_surface, (0 - ax, 0 - ay))

    if (ax != 0) and (ay == 0):
        while ax != 1:
            screen.blit(lv1_dark, (-ax, 0))
            if ax <= 0:
                ax += 1
            else:
                ax -= 1
    elif (ax == 0) and (ay != 0):
        while ay != 0:
            screen.blit(lv1_dark, (0, -ay))
            if ay <= 0:
                ay += 1
            else:
                ay -= 1
    elif (ax != 0) and (ay != 0):
        while ax != 0:
            screen.blit(lv1_dark, (-ax, -ay))
            if ax <= 0:
                ax += 1
            else:
                ax -= 1
            if ay <= 0:
                ay += 1
            else:
                ay -= 1
    screen.blit(level_1_surface, (0, 0))
    screen.blit(level_1_dang, (0 - ax, 0 - ay))
    screen.blit(finish, (x_finish, y_finish))


def draw_ball(screen, ball_surface, ball):
    screen.blit(ball_surface, (ball.x, ball.y))
