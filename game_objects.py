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

    def masks(self, level_mask, ball_mask, trap_mask):
        overlap_walls_level = level_mask.overlap(ball_mask, (self.x+self.vx-0, self.y+self.vy-0))
        overlap_walls_ball = ball_mask.overlap(level_mask, (0 - self.x-self.vx, 0 - self.y-self.vy))
        overlap_traps = trap_mask.overlap(ball_mask, (self.x-0, self.y-0))
        print(overlap_walls_ball, overlap_walls_level)
        if overlap_walls_level:
            #self.vx = -self.vx//2
            #self.vy = -self.vy//2
            if (overlap_walls_ball[0] <= 3) or (overlap_walls_ball[0] >= 63):
                self.vx = -self.vx
            if (overlap_walls_ball[1] <= 3) or (overlap_walls_ball[1] >= 63):
                self.vy = -self.vy
        self.x += self.vx
        self.y += self.vy
        if overlap_traps:
            self.x = 100
            self.y = 100
            self.vx = 0
            self.vy = 0
            self.ax = 0
            self.ay = 0

    def finish(self, ball_mask, finish_mask):
        overlap_finish = finish_mask.overlap(ball_mask, (self.x + self.vx - 0, self.y + self.vy - 0))
        if overlap_finish:
            running = False
        return running
