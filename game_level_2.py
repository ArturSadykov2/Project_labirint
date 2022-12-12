import pygame as pg
from game_texture_Artur import *
from game_texture_oleg import *
from game_levels_graphics import draw_ball, draw_level
from game_objects_ball import Ball
from game_object_gun import Bullet
from game_object_disk import Disk


def level_2(screensize, ball_surf, menu):
    x2 = 600
    y2 = 280
    xf2 = 1050
    yf2 = 650
    bullets = []
    k = 0
    delay = 120
    screen = pg.display.set_mode(screensize)
    clock = pg.time.Clock()
    ball_surface = ball_surf
    ball_mask = pg.mask.from_surface(ball_surface)
    level_mask = pg.mask.from_surface(lv2_walls_surf)
    trap_mask = pg.mask.from_surface(lv2_traps_surf)
    ball_x_mask = pg.mask.from_surface(ball_x_surf)
    ball_y_mask = pg.mask.from_surface(ball_y_surf)
    finish_mask = pg.mask.from_surface(finish_surf)
    running = True
    ball = Ball(x2, y2)
    ball.__init__(x2, y2)
    floor_disk = Disk(550, 450, 0.5, 0, disk_floor_surf)
    wall_disk = Disk(550, 450, 0.5, 0, disk_walls_surf)
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
        floor_disk.move()
        wall_disk.move()
        k += 1
        if k >= delay:
            k = 0
            bullets.append(Bullet(500, 80, 0, 2))
        if bullets:
            for i in range(len(bullets)):
                b = bullets[i]
                b.move()
                kill, kill_ball = b.collusion(level_mask, ball, x2, y2, ball_mask)
                if kill:
                    del bullets[i]
                    break
                if kill_ball:
                    bullets = []
                    break
        Ball.collusion(ball, level_mask, ball_mask, trap_mask, ball_x_mask, ball_y_mask, x2, y2)
        wall_disk.collusion(ball, ball_x_mask, ball_y_mask)
        draw_level(screen, lv2_walls_surf, lv2_traps_surf, bg_wood_surface, ball, finish_surf, xf2, yf2, lv2_dark_surf)
        floor_disk.draw(screen)
        if bullets:
            for b in bullets:
                b.draw(screen)
        draw_ball(screen, ball_surface, ball)
        running = ball.finish(ball_mask, finish_mask, menu, xf2, yf2, running)
        pg.display.flip()
        clock.tick(60)
