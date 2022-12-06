import pygame as pg
import math
from random import choice, randint
from game_texture import *
from Graphics import *
from Events import *
from Objects import Ball
"""Вызывается из меню, сама вызывает функции отрисовки и расчета физики"""


def level_1(screensize, mid_screen, ball_texture):
    screen = pg.display.set_mode(screensize)
    clock = pg.time.Clock()
    set_level_textures(screensize, level1, mid_screen)
    running = True
    ball = Ball()
    ball.__init__(100, 100, ball_texture)
    while running:
        for event in pg.event.get():
            move_events(event, ball)
