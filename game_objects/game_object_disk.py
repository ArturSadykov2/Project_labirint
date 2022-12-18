from game_texture import *
from numpy import pi


class Disk:
    """
    Class of rotating disk
    """
    def __init__(self, x, y, w, angle, surf):
        """
        Set start values
        :param x: x coordinate of disk center
        :param y: y coordinate of disk center
        :param w: angle speed
        :param angle: angle, on that rotated disk
        :param surf: texture of disk
        """
        self.x = x
        self.y = y
        self.w = w
        self.angle = angle
        self.surf = surf

    def move(self, dt):
        """
        Function, that rotated disk
        :param dt: time interval
        """
        self.angle += self.w * dt

    def draw(self, screen):
        """
        Draw disk
        :param screen: screen in pygame, where function draw object
        """
        rect = self.surf.get_rect(center=(self.x, self.y))
        rotated_disk = pg.transform.rotate(self.surf, self.angle)
        rot_rect = rotated_disk.get_rect(center=rect.center)
        screen.blit(rotated_disk, rot_rect)

    def collusion(self, ball, ball_mask, dt):
        """
        Check collusion ball with disk
        :param ball: object in class Ball
        :param ball_mask: pygame mask of ball
        :param dt: time interval
        """
        rect = self.surf.get_rect(center=(self.x, self.y))
        rotated_disk = pg.transform.rotate(self.surf, self.angle)
        rot_rect = rotated_disk.get_rect(center=rect.center)
        mask = pg.mask.from_surface(rotated_disk)
        overlap_x = mask.overlap(ball_mask, (ball.x + ball.vx - rot_rect[0], ball.y - rot_rect[1]))
        overlap_y = mask.overlap(ball_mask, (ball.x - rot_rect[0], ball.y + ball.vy - rot_rect[1]))
        if overlap_x:
            if ball.vx == 0:
                ball.vx = - self.w * ((ball.x + ball.vx) - self.x)/pi * dt
            else:
                ball.vx = -ball.vx
        if overlap_y:
            if ball.vy == 0:
                ball.vy = - self.w * ((ball.y + ball.vy) - self.y)/pi * dt
            else:
                ball.vy = -ball.vy
