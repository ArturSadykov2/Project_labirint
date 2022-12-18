from game_objects.game_levels_graphics import draw_ball, draw_level, Wall
from game_objects.game_objects_ball import Ball
from game_objects.game_object_gun import Bullet
from game_texture import *

pg.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512, devicename=None)
pg.init()


def level_3(screensize, ball_surf, menu, balls_surfaces, channel):
    """
        That function start 3-rd level
        :param screensize: size of screen
        :param ball_surf: ball texture, that was set in settings
        :param menu: object in class Menu
        :param balls_surfaces: massive with ball textures
        :param channel:
    """
    x3, y3 = coord_of_start[2]
    xf3, yf3 = coord_of_finish[2]
    bullets = []
    delay = 240
    k = 240
    fps = 60
    screen = pg.display.set_mode(screensize)
    clock = pg.time.Clock()
    ball_surface = ball_surf
    ball_mask = pg.mask.from_surface(ball_surface)
    level_mask = pg.mask.from_surface(lv3_dark)
    trap_mask = pg.mask.from_surface(lv3_traps_surf)
    finish_mask = pg.mask.from_surface(finish_surf)
    running = True
    ball = Ball(x3, y3)
    ball.__init__(x3, y3)
    wall = Wall()
    wall.__init__()
    while running:
        if fps != 0:
            dt = 1 / fps
        else:
            dt = 1 / 60
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE and not menu.menu_live:
                    menu.menu_live = 1
                    menu.pause_menu = 1
                    coord_of_start[2][0] = ball.x
                    coord_of_start[2][1] = ball.y
                    running = False
        ball.ball_boost()
        ball.play_music(channel, bounce_sound)
        Ball.ball_move(ball, dt)
        k += 1
        if k >= delay:
            k = 0
            bullets.append(Bullet(75, 140, 1.57, 120, balls_surfaces))
            bullets.append(Bullet(1245, 570, -1.57, 120, balls_surfaces))
        if bullets:
            for i in range(len(bullets)):
                b = bullets[i]
                b.move(dt)
                kill, kill_ball = b.collusion(level_mask, ball, x3, y3, ball_mask, dt)
                if kill:
                    del bullets[i]
                    break
                if kill_ball:
                    bullets = []
                    break
        Ball.collusion(ball, level_mask, ball_mask, trap_mask, x3, y3)
        draw_level(screen, lv3_walls_surf, lv3_traps_surf, bg_wood_surface,
                   ball, finish_surf, xf3, yf3, lv3_dark_surf, wall)
        if bullets:
            for b in bullets:
                b.draw(screen)
        draw_ball(screen, ball_surface, ball)
        running = ball.finish(ball_mask, finish_mask, menu, xf3, yf3, running)
        pg.display.flip()
        clock.tick(60)
        fps = clock.get_fps()
        print(clock.get_fps())
