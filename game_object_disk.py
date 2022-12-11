import pygame as pg
from game_texture_Artur import *


class Disk:
    def __init__(self, x, y, w, angle, surf):
        self.x = x
        self.y = y
        self.w = w
        self.angle = angle
        self.surf = surf

    def move(self):
        self.angle += self.w

    def draw(self, screen):
        rect = self.surf.get_rect(center=(self.x, self.y))
        rotated_disk = pg.transform.rotate(self.surf, self.angle)
        rot_rect = rotated_disk.get_rect(center=rect.center)
        screen.blit(rotated_disk, rot_rect)

    def collusion(self, ball, ball_x_mask, ball_y_mask):
        rect = self.surf.get_rect(center=(self.x, self.y))
        rotated_disk = pg.transform.rotate(self.surf, self.angle)
        rot_rect = rotated_disk.get_rect(center=rect.center)
        mask = pg.mask.from_surface(rotated_disk)
        overlap_x = mask.overlap(ball_x_mask, (ball.x + ball.vx - rot_rect[0], ball.y + ball.vy - rot_rect[1]))
        overlap_y = mask.overlap(ball_y_mask, (ball.x + ball.vx - rot_rect[0], ball.y + ball.vy - rot_rect[1]))
        r = ((self.x - (ball.x + ball.vx))**2 + (self.y - (ball.y + ball.vy))**2)**0.5
        if overlap_x:
            ball.vx = -ball.vx #- self.w * ((ball.x + ball.vx) - self.x)
        if overlap_y:
            ball.vy = -ball.vy #- self.w * ((ball.y + ball.vy) - self.y)
