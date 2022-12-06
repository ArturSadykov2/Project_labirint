import pygame as pg


class Ball:
    def __init__(self, ball_x, ball_y, ball_texture):
        self.x = ball_x
        self.y = ball_y
        self.texture = ball_texture
        self.ax = 0
        self.ay = 0

    def ball_boost(self):
        for event in pg.event.get():
            keys = pg.key.get_pressed()
            if keys[pg.K_DOWN]:
                self.ay = 5
            if keys[pg.K_LEFT]:
                self.ax = -5
            if keys[pg.K_UP]:
                self.ay = 5
            if keys[pg.K_RIGHT]:
                self.ax = 5