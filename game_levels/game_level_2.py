from game_objects.game_levels_graphics import draw_ball, draw_level, Wall
from game_objects.game_objects_ball import Ball
from game_objects.game_object_gun import Bullet
from game_objects.game_object_disk import Disk
from game_texture import *


pg.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512, devicename=None)
pg.init()


def level_2(screensize, ball_surf, menu, balls_surfaces, channel):
    """
        That function start 2-nd level
        :param screensize: size of screen
        :param ball_surf: ball texture, that was set in settings
        :param menu: object in class Menu
        :param balls_surfaces: massive with ball textures
        :param channel:
    """
    x2, y2 = coord_of_start[1]
    xf2, yf2 = coord_of_finish[1]
    bullets = []
    k = 180
    delay = 180
    fps = 60
    screen = pg.display.set_mode(screensize)
    clock = pg.time.Clock()
    ball_surface = ball_surf
    ball_mask = pg.mask.from_surface(ball_surface)
    bullet_level_mask = pg.mask.from_surface(lv2_dark_surf)
    ball_level_mask = pg.mask.from_surface(lv2_walls_surf)
    trap_mask = pg.mask.from_surface(lv2_traps_surf)
    finish_mask = pg.mask.from_surface(finish_surf)
    running = True
    ball = Ball(x2, y2)
    ball.__init__(x2, y2)
    floor_disk = Disk(550, 450, 30, 0, disk_floor_surf)
    wall_disk = Disk(550, 450, 30, 0, disk_walls_surf)
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
                    coord_of_start[1][0] = ball.x
                    coord_of_start[1][1] = ball.y
                    running = False
        ball.ball_boost()
        ball.play_music(channel, bounce_sound)
        Ball.ball_move(ball, dt)
        floor_disk.move(dt)
        wall_disk.move(dt)
        k += 1
        if k >= delay:
            k = 0
            bullets.append(Bullet(400, 80, 0, 120, balls_surfaces))
        if bullets:
            for i in range(len(bullets)):
                b = bullets[i]
                b.move(dt)
                kill, kill_ball = b.collusion(bullet_level_mask, ball, x2, y2, ball_mask, dt)
                if kill:
                    del bullets[i]
                    break
                if kill_ball:
                    bullets = []
                    break
        Ball.collusion(ball, ball_level_mask, ball_mask, trap_mask, x2, y2)
        wall_disk.collusion(ball, ball_mask, dt)
        draw_level(screen, lv2_walls_surf, lv2_traps_surf, bg_wood_surface,
                   ball, finish_surf, xf2, yf2, lv2_dark_surf, wall)
        floor_disk.draw(screen)
        if bullets:
            for b in bullets:
                b.draw(screen)
        draw_ball(screen, ball_surface, ball)
        running = ball.finish(ball_mask, finish_mask, menu, xf2, yf2, running)
        pg.display.flip()
        clock.tick(60)
        fps = clock.get_fps()
