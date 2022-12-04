import pygame as pg
import math
from random import choice, randint


bg_surface = pg.Surface((1280, 720), pg.SRCALPHA)
image = pg.image.load('file.png').convert_alpha()