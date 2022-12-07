import pygame as pg
from global_values import *
import os

pg.init()
size=[size_hight,size_width]

# load main game textures
home_screen_png = pg.image.load("image\main_backgroubd.png")
settings_screen_png = pg.image.load(os.path.join("image", "menu_ball.png"))
middle_screen_png = pg.image.load(os.path.join("image", "background.png"))

# load game textures
dark_ball_png = pg.image.load(os.path.join("image", "dark_ball.png"))
disco_ball_png = pg.image.load(os.path.join("image", "disco_ball.png"))
grey_ball_png = pg.image.load(os.path.join("image", "grey_ball.png"))
red_ball_png = pg.image.load(os.path.join("image", "red_ball.png"))
striped_ball_png = pg.image.load(os.path.join("image", "striped_ball.png"))
magma_ball_png = pg.image.load(os.path.join("image", "magma_ball.png"))

go_png = pg.image.load(os.path.join("image", "go_down.png"))
exit_png = pg.image.load(os.path.join("image", "exit_down.png"))
nextlvl_png = pg.image.load(os.path.join("image", "nextlvl_down.png"))
settings_png = pg.image.load(os.path.join("image", "settings_down.png"))

dark_down_png = pg.image.load(os.path.join("image", "dark_down.png"))
disco_down_png = pg.image.load(os.path.join("image", "disco_down.png"))
grey_down_png = pg.image.load(os.path.join("image", "grey_down.png"))
red_down_png = pg.image.load(os.path.join("image", "red_down.png"))
striped_down_png = pg.image.load(os.path.join("image", "striped_down.png"))
magma_down_png = pg.image.load(os.path.join("image", "magma_down.png"))

<<<<<<< HEAD
#creating surfaces for objects 

#creating main sirfaace
home = pg.transform.scale(home_screen_png, size)
home_surface = pg.Surface(size, pg.SRCALPHA)
home_surface.blit(home, (0, 0))

menu_of_set = pg.transform.scale(settings_screen_png, size)
menu_of_set_surface = pg.Surface(size, pg.SRCALPHA)
menu_of_set_surface.blit(menu_of_set, (0, 0))

middle = pg.transform.scale(middle_screen_png, size)
middle_surface = pg.Surface(size, pg.SRCALPHA)
middle_surface.blit(middle, (0, 0))

#creating surface for button

exitt = pg.transform.scale(exit_png, (281/1024*size_hight,93/576*size_width))
exit_surface = pg.Surface((281/1024*size_hight,93/576*size_width), pg.SRCALPHA)
exit_surface.blit(exitt, (0,0))

go = pg.transform.scale(go_png, (208/1024*size_hight,108/576*size_width))
go_surface = pg.Surface((208/1024*size_hight,108/576*size_width), pg.SRCALPHA)
go_surface.blit(go, (0,0))

settings = pg.transform.scale(settings_png, (320/1024*size_hight,107/576*size_width))
settings_surface = pg.Surface((320/1024*size_hight,107/576*size_width), pg.SRCALPHA)
settings_surface.blit(settings, (0,0))

nextlvl = pg.transform.scale(nextlvl_png, (281/1024*size_hight,92/576*size_width))
nextlvl_surface = pg.Surface((281/1024*size_hight,92/576*size_width), pg.SRCALPHA)
nextlvl_surface.blit(nextlvl, (0,0))

#creating buttons for selecting balls

dark_down = pg.transform.scale(dark_down_png, (215/1024*size_hight,215/576*size_width))
dark_button_surface = pg.Surface((215/1024*size_hight,215/576*size_width), pg.SRCALPHA)
dark_button_surface.blit(dark_down, (0,0))

disco_down = pg.transform.scale(disco_down_png, (215/1024*size_hight,215/576*size_width))
disco_button_surface = pg.Surface((215/1024*size_hight,215/576*size_width), pg.SRCALPHA)
disco_button_surface.blit(disco_down, (0,0))

grey_down = pg.transform.scale(grey_down_png, (215/1024*size_hight,215/576*size_width))
grey_button_surface = pg.Surface((215/1024*size_hight,215/576*size_width), pg.SRCALPHA)
grey_button_surface.blit(grey_down, (0,0))

red_down = pg.transform.scale(red_down_png, (215/1024*size_hight,215/576*size_width))
red_button_surface = pg.Surface((215/1024*size_hight,215/576*size_width), pg.SRCALPHA)
red_button_surface.blit(red_down, (0,0))

striped_down = pg.transform.scale(striped_down_png, (215/1024*size_hight,215/576*size_width))
striped_button_surface = pg.Surface((215/1024*size_hight,215/576*size_width), pg.SRCALPHA)
striped_button_surface.blit(striped_down, (0,0))

magma_down = pg.transform.scale(magma_down_png, (215/1024*size_hight,215/576*size_width))
magma_button_surface = pg.Surface((215/1024*size_hight,215/576*size_width), pg.SRCALPHA)
magma_button_surface.blit(magma_down, (0,0))

'''
=======
# Level textures
lv1_light = pg.image.load(os.path.join("lv1_light.png"))

'''screen = pg.display.set_mode(screen_size)
>>>>>>> 33486ba68f7b9847c3d721117d7bf98dbc5399fd
bg_texture = pg.transform.scale(bg_texture, size)
level_texture = pg.transform.scale(level_texture, size)
bg_surface = pg.Surface(size, pg.SRCALPHA)
bg_surface.blit(bg_texture, (0, 0))
labirint_surface = pg.Surface(size, pg.SRCALPHA)
labirint_surface.blit(level_texture, (0, 0))
labirint_mask = pg.mask.from_surface(labirint_surface)'''
<<<<<<< HEAD
=======


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
>>>>>>> 33486ba68f7b9847c3d721117d7bf98dbc5399fd
