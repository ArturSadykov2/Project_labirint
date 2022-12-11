import pygame as pg
import math
from random import choice, randint
from game_texture_Artur import *
from game_objects_ball import Ball


def draw_level(screen, lv_surface, lv_traps, bg_surface, ball, finish, x_finish, y_finish, lv_dark):
    ax = int(ball.ax * 30)
    ay = int(ball.ay * 30)
    screen.blit(bg_surface, (0 - ax, 0 - ay))

    if (ax != 0) and (ay == 0):
        while ax != 0:
            screen.blit(lv_dark, (-ax, 0))
            if ax <= 0:
                ax += 1
            else:
                ax -= 1
    elif (ax == 0) and (ay != 0):
        while ay != 0:
            screen.blit(lv_dark, (0, -ay))
            if ay <= 0:
                ay += 1
            else:
                ay -= 1
    elif (ax != 0) and (ay != 0):
        while ax != 0:
            screen.blit(lv_dark, (-ax, -ay))
            if ax <= 0:
                ax += 1
            else:
                ax -= 1
            if ay <= 0:
                ay += 1
            else:
                ay -= 1
    screen.blit(lv_surface, (0, 0))
    screen.blit(lv_traps, (0 - ax, 0 - ay))
    screen.blit(finish, (x_finish, y_finish))


def draw_ball(screen, ball_surface, ball):
    screen.blit(ball_surface, (ball.x, ball.y))
