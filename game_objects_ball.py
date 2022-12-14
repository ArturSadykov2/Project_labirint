import pygame as pg
from game_texture_oleg import *
from global_values import *

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ax = 0
        self.ay = 0
        self.vx = 0
        self.vy = 0

    def ball_boost(self, dt):
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

    def ball_move(self, dt):
        if abs(self.vx) <= 600 * dt:
            self.vx += self.ax
        if abs(self.vy) <= 600 * dt:
            self.vy += self.ay
        if self.vx != 0:
            if 6 * dt >= abs(self.vx):
                self.vx = 0
            elif self.vx >= 0:
                self.vx -= 6 * dt
            else:
                self.vx += 6 * dt
        if self.vy != 0:
            if 6 * dt >= abs(self.vy):
                self.vy = 0
            elif self.vy >= 0:
                self.vy -= 6 * dt
            else:
                self.vy += 6 * dt

    def collusion(self, level_mask, ball_mask, trap_mask, x, y):
        overlap_walls_x = level_mask.overlap(ball_mask, (self.x+self.vx-0, self.y-0))
        overlap_walls_y = level_mask.overlap(ball_mask, (self.x-0, self.y+self.vy-0))
        overlap_traps = trap_mask.overlap(ball_mask, (self.x+self.vx-0, self.y+self.vy-0))
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
            if obj.level_1:
                coord_of_start[0]=[90,80]
            elif obj.level_2:
                coord_of_start[1]=[100,80]
            elif obj.level_3:
                coord_of_start[2]=[1250,75]
            elif obj.level_4:
                coord_of_start[3]=[100,360]
                obj.intermediate_menu = 0
                obj.home_surface = 1
        return running
