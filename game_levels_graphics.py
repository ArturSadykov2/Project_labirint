class Wall:
    """
    Class with walls coordinates, that used to turning level
    """
    def __init__(self):
        self.x = 0
        self.y = 0


def draw_level(screen, lv_surface, lv_traps, bg_surface, ball, finish, x_finish, y_finish, lv_dark, wall):
    """
    Draw background, walls, traps, finish.
    :param screen: screen in pygame, where function draw all object
    :param lv_surface: surface with level walls
    :param lv_traps: surface with traps
    :param bg_surface: surface with background image
    :param ball: object in class Ball
    :param finish: surface with finish image
    :param x_finish: x coordinate of finish surface
    :param y_finish: y coordinate of finish surface
    :param lv_dark: surface with level dark walls
    :param wall: object in class Wall
    """
    if wall.x < int(ball.ax * 30):
        wall.x += 1
    if wall.x > int(ball.ax * 30):
        wall.x -= 1
    if wall.y < int(ball.ay * 30):
        wall.y += 1
    if wall.y > int(ball.ay * 30):
        wall.y -= 1
    screen.blit(bg_surface, (0 - wall.x, 0 - wall.y))
    ax = wall.x
    ay = wall.y

    if (ax != 0) and (ay == 0):
        while ax != 0:
            screen.blit(lv_dark, (-ax, 0))
            if ax <= 0:
                ax += 1
            else:
                ax -= 1
    elif (ax == 0) and (ay != 0):
        while ay != 0:
            screen.blit(lv_dark, (0, -ay))
            if ay <= 0:
                ay += 1
            else:
                ay -= 1
    elif (ax != 0) and (ay != 0):
        while ax != 0:
            screen.blit(lv_dark, (-ax, -ay))
            if ax <= 0:
                ax += 1
            else:
                ax -= 1
            if ay <= 0:
                ay += 1
            else:
                ay -= 1
    screen.blit(lv_traps, (0 - wall.x, 0 - wall.y))
    screen.blit(lv_surface, (0, 0))
    screen.blit(finish, (x_finish, y_finish))


def draw_ball(screen, ball_surface, ball):
    """
    Draw ball on screen
    :param screen: screen in pygame, where function draw object
    :param ball_surface: ball texture, that was select in settings
    :param ball: object in class Ball
    """
    screen.blit(ball_surface, (ball.x, ball.y))
