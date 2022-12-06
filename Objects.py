import pygame as pg
from game_texture import *

class Ball:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.texture = disco_ball
        self.ax = 0
        self.ay = 0

    def ball_boost(self):
        if pg.key.get_pressed()[pg.K_DOWN]:
            self.ay = -10
        if pg.key.get_pressed()[pg.K_LEFT]:
            self.ax = -10
        if pg.key.get_pressed()[pg.K_UP]:
            self.ay = 10
        if pg.key.get_pressed()[pg.K_RIGHT]:
            self.ax = 10
