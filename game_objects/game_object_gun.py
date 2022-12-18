from numpy import sin, cos
from random import randint
from game_texture import bullet_mask


class Bullet:
    """Класс, отрисовывающий снаряд"""
    def __init__(self, x, y, angle, v, balls_surfaces):
        """
        Set start values
        :param x: x coordinate of start bullet position
        :param y: y coordinate of start bullet position
        :param angle: angle between speed direction and horizontal
        :param v: bullet speed
        :param balls_surfaces: massive with ball textures
        """
        self.points = 0
        self.x = x
        self.y = y
        self.vx = v * cos(angle)
        self.vy = v * sin(angle)
        self.angle = angle
        self.surf = balls_surfaces[randint(2, 5)]
        self.mask = bullet_mask

    def draw(self, screen):
        """
        Draw bullet
        :param screen: screen in pygame, where function draw object
        """
        screen.blit(self.surf, (self.x, self.y))

    def move(self, dt):
        """
        Calculate bullet coordinates
        :param dt: time interval
        """
        self.x += self.vx * dt
        self.y += self.vy * dt

    def collusion(self, wall_mask, ball, x, y, ball_mask, dt):
        """
        Check collusion bullets with walls and ball
        :param wall_mask: mask with level walls
        :param ball: object in class Ball
        :param x: start ball x position
        :param y: start ball y position
        :param ball_mask: pygame mask of ball
        :param dt: time interval
        """
        overlap_wall = wall_mask.overlap(self.mask, (self.x+self.vx * dt-0, self.y+self.vy * dt-0))
        overlap_ball = ball_mask.overlap(self.mask,
                                         (self.x + self.vx * dt - ball.x - ball.vx,
                                          self.y + self.vy * dt - ball.y - ball.vy))
        kill_ball = False
        kill = False
        if overlap_ball:
            ball.x = x
            ball.y = y
            ball.vx = 0
            ball.vy = 0
            ball.ax = 0
            ball.ay = 0
            kill_ball = True
        if overlap_wall:
            kill = True
        return kill, kill_ball
