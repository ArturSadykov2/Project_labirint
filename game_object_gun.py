import pygame as pg
import math
from random import choice, randint
from game_texture_Artur import *
from game_texture_oleg import *
from game_levels_graphics import *
from game_objects_ball import Ball


class Bullet:
    """Класс, отрисовывающий снаряд"""
    def __init__(self, x, y, angle, v, balls_surfaces, dt):
        self.points = 0
        self.x = x  # gun.x
        self.y = y  # gun.y
        self.vx = v * math.cos(angle)
        self.vy = v * math.sin(angle)
        self.angle = angle  # gun.angle
        self.surf = balls_surfaces[randint(2, 5)]
        self.mask = bullet_mask

    def draw(self, screen):
        """Функия, отрисовывающая мишень в сгенерированных координатах"""
        screen.blit(self.surf, (self.x, self.y))

    def move(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

    def collusion(self, wall_mask, ball, x, y, ball_mask, dt):
        overlap_wall = wall_mask.overlap(self.mask, (self.x+self.vx * dt-0, self.y+self.vy * dt-0))
        overlap_ball = ball_mask.overlap(self.mask,
                                         (self.x + self.vx * dt - ball.x - ball.vx,
                                          self.y + self.vy * dt - ball.y - ball.vy))
        kill_ball = False
        kill = False
        if overlap_ball:
            ball.x = x
            ball.y = y
            ball.vx = 0
            ball.vy = 0
            ball.ax = 0
            ball.ay = 0
            kill_ball = True
        if overlap_wall:
            kill = True
        return kill, kill_ball
