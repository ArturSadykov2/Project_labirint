import pygame as pg
from game_texture_oleg import *


class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
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
        if abs(self.vx) <= 10:
            self.vx += self.ax
        if abs(self.vy) <= 10:
            self.vy += self.ay
        if self.vx != 0:
            if 0.1 >= abs(self.vx):
                self.vx = 0
            elif self.vx >= 0:
                self.vx -= 0.1
            else:
                self.vx += 0.1
        if self.vy != 0:
            if 0.1 >= abs(self.vy):
                self.vy = 0
            elif self.vy >= 0:
                self.vy -= 0.1
            else:
                self.vy += 0.1

    def collusion(self, level_mask, ball_mask, trap_mask, ball_x_mask, ball_y_mask, x, y):
        overlap_walls_x = level_mask.overlap(ball_x_mask, (self.x+self.vx-0, self.y+self.vy-0))
        overlap_walls_y = level_mask.overlap(ball_y_mask, (self.x+self.vx-0, self.y+self.vy-0))
        overlap_traps = trap_mask.overlap(ball_mask, (self.x-0, self.y-0))
        if overlap_walls_x:
            self.vx = -self.vx
        if overlap_walls_y:
            self.vy = -self.vy
        self.x += self.vx
        self.y += self.vy
        if overlap_traps:
            self.x = x
            self.y = y
            self.vx = 0
            self.vy = 0
            self.ax = 0
            self.ay = 0

    def finish(self, ball_mask, finish_mask, obj, x_finish, y_finish, running):
        overlap_finish = finish_mask.overlap(ball_mask, (x_finish - self.x + self.vx, y_finish - self.y + self.vy))
        if overlap_finish:
            running = False
            obj.menu_live = 1
            obj.intermediate_menu = 1
        return running