import pygame as pg
from game_texture_oleg import *


class Ball:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.ax = 0
        self.ay = 0
        self.vx = 0
        self.vy = 0

    def ball_boost(self):
        a = 0.33
        if pg.key.get_pressed()[pg.K_s] or pg.key.get_pressed()[pg.K_DOWN]:
            self.ay = a
        elif pg.key.get_pressed()[pg.K_w] or pg.key.get_pressed()[pg.K_UP]:
            self.ay = -a
        else:
            self.ay = 0
        if pg.key.get_pressed()[pg.K_a] or pg.key.get_pressed()[pg.K_LEFT]:
            self.ax = -a
        elif pg.key.get_pressed()[pg.K_d] or pg.key.get_pressed()[pg.K_RIGHT]:
            self.ax = a
        else:
            self.ax = 0

    def ball_move(self):
        self.vx += self.ax
        self.vy += self.ay
        if self.vx != 0:
            if abs(0.1*abs(self.vx)/self.vx) >= abs(self.vx):
                self.vx = 0
            else:
                self.vx -= (0.1*abs(self.vx)/self.vx)
        if self.vy != 0:
            if abs(0.1*abs(self.vy)/self.vy) >= abs(self.vy):
                self.vy = 0
            else:
                self.vy -= (0.1*abs(self.vy)/self.vy)
        self.x += self.vx
        self.y += self.vy
