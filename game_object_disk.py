import pygame as pg
from game_texture_Artur import *
import numpy as np


class Disk:
    def __init__(self, x, y, w, angle, surf):
        self.x = x
        self.y = y
        self.w = w
        self.angle = angle
        self.surf = surf

    def move(self, dt):
        self.angle += self.w * dt

    def draw(self, screen):
        rect = self.surf.get_rect(center=(self.x, self.y))
        rotated_disk = pg.transform.rotate(self.surf, self.angle)
        rot_rect = rotated_disk.get_rect(center=rect.center)
        screen.blit(rotated_disk, rot_rect)

    def collusion(self, ball, ball_mask):
        rect = self.surf.get_rect(center=(self.x, self.y))
        rotated_disk = pg.transform.rotate(self.surf, self.angle)
        rot_rect = rotated_disk.get_rect(center=rect.center)
        mask = pg.mask.from_surface(rotated_disk)
        overlap_x = mask.overlap(ball_mask, (ball.x + ball.vx - rot_rect[0], ball.y - rot_rect[1]))
        overlap_y = mask.overlap(ball_mask, (ball.x - rot_rect[0], ball.y + ball.vy - rot_rect[1]))
        r = ((self.x - (ball.x + ball.vx))**2 + (self.y - (ball.y + ball.vy))**2)**0.5
        if overlap_x:
            if ball.vx == 0:
                ball.vx = - self.w * ((ball.x + ball.vx) - self.x)/np.pi
            else:
                ball.vx = -ball.vx
        if overlap_y:
            if ball.vy == 0:
                ball.vy = - self.w * ((ball.y + ball.vy) - self.y)/np.pi
            else:
                ball.vy = -ball.vy
