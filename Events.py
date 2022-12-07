import pygame as pg
# from Objects import Ball


def move_events(event, ball):
    for event in pg.event.get():
        keys = pg.key.get_pressed()
        if keys[pg.K_DOWN]:
            ball.ay = 5
        if keys[pg.K_LEFT]:
            ball.ax = -5
        if keys[pg.K_UP]:
            ball.ay = 5
        if keys[pg.K_RIGHT]:
            ball.ax = 5
