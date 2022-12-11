import pygame as pg
import math
from random import choice, randint
from game_texture_Artur import *
from game_texture_oleg import *
from game_levels_graphics import *
from game_objects_ball import Ball
BLACK = (0, 0, 0)


class Bullet:
    """Класс, отрисовывающий мишень в случайной точке"""
    def __init__(self, x, y):
        self.points = 0
        self.x = x  # gun.x
        self.y = y  # gun.y
        self.color = BLACK
        self.v = 1
        self.angle = 0  # gun.angle
        self.surf = dark_ball_surface

    def draw(self, screen):
        """Функия, отрисовывающая мишень в сгенерированных координатах"""
        screen.blit(self.surf, (self.x, self.y))
