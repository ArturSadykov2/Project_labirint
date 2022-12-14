import pygame as pg
import math
from random import choice, randint
from game_texture_Artur import *
from game_texture_oleg import *
from game_levels_graphics import *
from game_objects_ball import Ball
from game_object_gun import Bullet


def level_4(screensize, ball_surf, menu, balls_surfaces):
    x4 = 100
    y4 = 360
    xf4 = 1200
    yf4 = 360
    bullets = []
    delay = 600
    k = delay
    screen = pg.display.set_mode(screensize)
    clock = pg.time.Clock()
    ball_surface = ball_surf
    ball_mask = pg.mask.from_surface(ball_surface)
    level_mask = pg.mask.from_surface(lv4_walls_surf_g)
    trap_mask = pg.mask.from_surface(lv4_traps_surf)
    ball_x_mask = pg.mask.from_surface(ball_x_surf)
    ball_y_mask = pg.mask.from_surface(ball_y_surf)
    finish_mask = pg.mask.from_surface(finish_surf)
    running = True
    ball = Ball(x4, y4)
    ball.__init__(x4, y4)
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
            bullets.append(Bullet(150, 100, 0.785398, 2, balls_surfaces))
            bullets.append(Bullet(640, 100, 0.785398, 2, balls_surfaces))
            bullets.append(Bullet(150, 620, -0.785398, 2, balls_surfaces))
            bullets.append(Bullet(640, 620, -0.785398, 2, balls_surfaces))
        if bullets:
            for i in range(len(bullets)):
                b = bullets[i]
                b.move()
                kill, kill_ball = b.collusion(level_mask, ball, x4, y4, ball_mask)
                if kill:
                    del bullets[i]
                    break
                if kill_ball:
                    bullets = []
                    break
        Ball.collusion(ball, level_mask, ball_mask, trap_mask, ball_x_mask, ball_y_mask, x4, y4)
        draw_level(screen, lv4_walls_surf, lv4_traps_surf, bg_wood_surface, ball, finish_surf, xf4, yf4, lv4_dark_surf)
        if bullets:
            for b in bullets:
                b.draw(screen)
        draw_ball(screen, ball_surface, ball)
        running = ball.finish(ball_mask, finish_mask, menu, xf4, yf4, running)
        pg.display.flip()
        clock.tick(60)
