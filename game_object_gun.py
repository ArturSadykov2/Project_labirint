import pygame as pg
import math
from random import choice, randint
from game_texture_Artur import *
from game_texture_oleg import *
from game_levels_graphics import *
from game_objects_ball import Ball
BLACK = (0, 0, 0)


class Target:
    """Класс, отрисовывающий мишень в случайной точке"""
    def __init__(self, gun):
        self.points = 0
        self.x = gun.x
        self.y = gun.y
        self.r = 20
        self.color = BLACK
        self.v = 1
        self.angle = gun.angle

    def hit(self, ball):
        """Попадание шарика в цель."""


    def draw(self, screen):
        """Функия, отрисовывающая мишень в сгенерированных координатах"""
        pg.draw.circle(screen, self.color, (self.x, self.y), self.r)
