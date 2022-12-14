import pygame as pg
import math
from random import choice, randint
from game_texture_Artur import *
from game_texture_oleg import *
from game_levels_graphics import draw_ball, draw_level, Wall
from game_objects_ball import Ball
from game_object_gun import Bullet


def level_3(screensize, ball_surf, menu, balls_surfaces):
    x3 = 1250
    y3 = 75
    xf3 = 970
    yf3 = 420
    bullets = []
    delay = 240
    k = 240
    screen = pg.display.set_mode(screensize)
    clock = pg.time.Clock()
    ball_surface = ball_surf
    ball_mask = pg.mask.from_surface(ball_surface)
    level_mask = pg.mask.from_surface(lv3_dark)
    trap_mask = pg.mask.from_surface(lv3_traps_surf)
    ball_x_mask = pg.mask.from_surface(ball_x_surf)
    ball_y_mask = pg.mask.from_surface(ball_y_surf)
    finish_mask = pg.mask.from_surface(finish_surf)
    running = True
    ball = Ball(x3, y3)
    ball.__init__(x3, y3)
    wall = Wall()
    wall.__init__()
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE and not menu.menu_live:
                    menu.menu_live = 1
                    menu.pause_menu = 1
                    running = False
        ball.ball_boost()
        Ball.ball_move(ball)
        k += 1
        if k >= delay:
            k = 0
            bullets.append(Bullet(75, 140, 1.57, 2, balls_surfaces))
            bullets.append(Bullet(1245, 570, -1.57, 2, balls_surfaces))
        if bullets:
            for i in range(len(bullets)):
                b = bullets[i]
                b.move()
                kill, kill_ball = b.collusion(level_mask, ball, x3, y3, ball_mask)
                if kill:
                    del bullets[i]
                    break
                if kill_ball:
                    bullets = []
                    break
        Ball.collusion(ball, level_mask, ball_mask, trap_mask, ball_x_mask, ball_y_mask, x3, y3)
        draw_level(screen, lv3_walls_surf, lv3_traps_surf, bg_wood_surface,
                   ball, finish_surf, xf3, yf3, lv3_dark_surf, wall)
        if bullets:
            for b in bullets:
                b.draw(screen)
        draw_ball(screen, ball_surface, ball)
        running = ball.finish(ball_mask, finish_mask, menu, xf3, yf3, running)
        pg.display.flip()
        clock.tick(60)
