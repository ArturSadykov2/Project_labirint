from game_objects.game_levels_graphics import draw_ball, draw_level, Wall
from game_objects.game_objects_ball import Ball
from game_texture import *


pg.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512, devicename=None)
pg.init()


def level_1(screensize, ball_surf, menu, channel):
    """
    That function start 1-st level
    :param screensize: size of screen
    :param ball_surf: ball texture, that was select in settings
    :param menu: object in class Menu
    :param channel:
    """
    x1, y1 = coord_of_start[0]
    xf1, yf1 = coord_of_finish[0]
    fps = 60
    screen = pg.display.set_mode(screensize)
    clock = pg.time.Clock()
    ball_surface = ball_surf
    ball_mask = pg.mask.from_surface(ball_surface)
    level_mask = pg.mask.from_surface(lv1_walls_surf)
    trap_mask = pg.mask.from_surface(lv1_traps_surf)
    finish_mask = pg.mask.from_surface(finish_surf)
    running = True
    ball = Ball(x1, y1)
    ball.__init__(x1, y1)
    wall = Wall()
    wall.__init__()
    while running:
        if fps != 0:
            dt = 1 / fps
        else:
            dt = 1/60
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE and not menu.menu_live:
                    menu.menu_live = 1
                    menu.pause_menu = 1
                    coord_of_start[0][0] = ball.x
                    coord_of_start[0][1] = ball.y
                    running = False
        ball.ball_boost()
        ball.play_music(channel, bounce_sound)
        Ball.ball_move(ball, dt)
        Ball.collusion(ball, level_mask, ball_mask, trap_mask, x1, y1)
        draw_level(screen, lv1_walls_surf, lv1_traps_surf, bg_wood_surface,
                   ball, finish_surf, xf1, yf1, lv1_dark_surf, wall)
        draw_ball(screen, ball_surface, ball)
        running = ball.finish(ball_mask, finish_mask, menu, xf1, yf1, running)
        pg.display.flip()
        clock.tick(60)
        fps = clock.get_fps()
