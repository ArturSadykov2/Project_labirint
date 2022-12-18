from game_objects.game_levels_graphics import draw_ball, draw_level, Wall
from game_objects.game_objects_ball import Ball
from game_objects.game_object_gun import Bullet
from game_texture import *

pg.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512, devicename=None)
pg.init()


def level_4(screensize, ball_surf, menu, balls_surfaces, channel):
    """
        That function start 4-th level
        :param screensize: size of screen
        :param ball_surf: ball texture, that was set in settings
        :param menu: object in class Menu
        :param balls_surfaces: massive with ball textures
        :param channel:
    """
    x4, y4 = coord_of_start[3]
    xf4, yf4 = coord_of_finish[3]
    bullets = []
    delay = 600
    k = delay
    fps = 60
    screen = pg.display.set_mode(screensize)
    clock = pg.time.Clock()
    ball_surface = ball_surf
    ball_mask = pg.mask.from_surface(ball_surface)
    level_mask = pg.mask.from_surface(lv4_walls_surf_g)
    trap_mask = pg.mask.from_surface(lv4_traps_surf)
    finish_mask = pg.mask.from_surface(finish_surf)
    running = True
    ball = Ball(x4, y4)
    ball.__init__(x4, y4)
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
                    coord_of_start[3][0] = ball.x
                    coord_of_start[3][1] = ball.y
                    running = False
        ball.ball_boost()
        ball.play_music(channel, bounce_sound)
        Ball.ball_move(ball, dt)
        k += 1
        if k >= delay:
            k = 0
            bullets.append(Bullet(150, 100, 0.785398, 120, balls_surfaces))
            bullets.append(Bullet(640, 100, 0.785398, 120, balls_surfaces))
            bullets.append(Bullet(150, 620, -0.785398, 120, balls_surfaces))
            bullets.append(Bullet(640, 620, -0.785398, 120, balls_surfaces))
        if bullets:
            for i in range(len(bullets)):
                b = bullets[i]
                b.move(dt)
                kill, kill_ball = b.collusion(level_mask, ball, x4, y4, ball_mask, dt)
                if kill:
                    del bullets[i]
                    break
                if kill_ball:
                    bullets = []
                    break
        Ball.collusion(ball, level_mask, ball_mask, trap_mask, x4, y4)
        draw_level(screen, lv4_walls_surf, lv4_traps_surf, bg_wood_surface,
                   ball, finish_surf, xf4, yf4, lv4_dark_surf, wall)
        if bullets:
            for b in bullets:
                b.draw(screen)
        draw_ball(screen, ball_surface, ball)
        running = ball.finish(ball_mask, finish_mask, menu, xf4, yf4, running)
        pg.display.flip()
        fps = clock.get_fps()
        clock.tick(60)
