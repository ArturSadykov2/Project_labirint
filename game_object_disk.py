import pygame as pg
from game_texture_Artur import *


class Disk:
    def __init__(self, x, y, w, angle, surf, mask):
        self.x = x
        self.y = y
        self.w = w
        self.angle = angle
        self.surf = surf
        self.mask = mask

    def draw(self, screen):
        rect = self.surf.get_rect(center=(self.x, self.y))
        rotated_disk = pg.transform.rotate(self.surf, self.angle)
        rot_rect = rotated_disk.get_rect(center=rect.center)
        screen.blit(rotated_disk, rot_rect)
