import pygame as pg
import numpy as np
import os

pg.init()
size = [1392, 783]

home_screen = pg.image.load("image\main_backgroubd.png")
menu_screen = pg.image.load(os.path.join("image", "menu_ball.png"))
mid_screen = pg.image.load(os.path.join("image", "background.png"))

# load balls textures
dark_ball = pg.image.load(os.path.join("image", "dark_ball.png"))
disco_ball = pg.image.load(os.path.join("image", "disco_ball.png"))
grey_ball = pg.image.load(os.path.join("image", "grey_ball.png"))
red_ball = pg.image.load(os.path.join("image", "red_ball.png"))
striped_ball = pg.image.load(os.path.join("image", "striped_ball.png"))
magma_ball = pg.image.load(os.path.join("image", "magma_ball.png"))

go = pg.image.load(os.path.join("image", "go_down.png"))
exitt = pg.image.load(os.path.join("image", "exit_down.png"))
nextlvl = pg.image.load(os.path.join("image", "nextlvl_down.png"))
settings = pg.image.load(os.path.join("image", "settings_down.png"))

dark_down = pg.image.load(os.path.join("image", "dark_down.png"))
disco_down = pg.image.load(os.path.join("image", "disco_down.png"))
grey_down = pg.image.load(os.path.join("image", "grey_down.png"))
red_down = pg.image.load(os.path.join("image", "red_down.png"))
striped_down = pg.image.load(os.path.join("image", "striped_down.png"))
magma_down = pg.image.load(os.path.join("image", "magma_down.png"))

# Level textures
lv1_light = pg.image.load(os.path.join("lv1_light.png"))

'''screen = pg.display.set_mode(screen_size)
bg_texture = pg.transform.scale(bg_texture, size)
level_texture = pg.transform.scale(level_texture, size)
bg_surface = pg.Surface(size, pg.SRCALPHA)
bg_surface.blit(bg_texture, (0, 0))
labirint_surface = pg.Surface(size, pg.SRCALPHA)
labirint_surface.blit(level_texture, (0, 0))
labirint_mask = pg.mask.from_surface(labirint_surface)'''


class Menu:
    '''
    Function that draws main Menu with options of choose the level and starting the game
    '''

    def __init__(self, screen):
        self.script = 1
        self.screen = screen
        # self.x = x

    # def check_on(self, event):
    # if (event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x)

    def draw(self):
        if self.script == 1:
            home = pg.transform.scale(home_screen, size)
            home_surface = pg.Surface(size)
            home_surface.blit(home, (0, 0))
            self.screen.blit(home_surface, (0, 0))


class Cursor:
    def __init__(self, screen, x=0, y=0):
        self.screen = screen
        self.y = y
        self.x = x

    def cursor_change_pos(self, event):
        self.x, self.y = event.pos[0], event.pos[1]

    def draw_cursor(self, r=10, Crimson=[220, 20, 60], BLACK=(0, 0, 0)):
        center = np.array([self.x, self.y])
        pg.draw.circle(self.screen, Crimson, center, r, round(r / 5))
        pg.draw.circle(self.screen, BLACK, center, 2)

        p1, p2 = [np.array([r / 2, 0]) + center, np.array([1.5 * r, 0]) + center]
        pg.draw.line(self.screen, Crimson, p1, p2, 3)

        c1, c2 = np.array([-r / 2, 0]) + center, np.array([-1.5 * r, 0]) + center
        pg.draw.line(self.screen, Crimson, c1, c2, 3)

        b1, b2 = np.array([0, r / 2]) + center, np.array([0, 1.5 * r]) + center
        pg.draw.line(self.screen, Crimson, b1, b2, 3)

        d1, d2 = np.array([0, -r / 2]) + center, np.array([0, -1.5 * r]) + center
        pg.draw.line(self.screen, Crimson, d1, d2, 3)
