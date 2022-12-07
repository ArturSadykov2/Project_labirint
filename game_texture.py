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

'''
bg_texture = pg.transform.scale(bg_texture, size)
level_texture = pg.transform.scale(level_texture, size)
bg_surface = pg.Surface(size, pg.SRCALPHA)
bg_surface.blit(bg_texture, (0, 0))
labirint_surface = pg.Surface(size, pg.SRCALPHA)
labirint_surface.blit(level_texture, (0, 0))
labirint_mask = pg.mask.from_surface(labirint_surface)'''
