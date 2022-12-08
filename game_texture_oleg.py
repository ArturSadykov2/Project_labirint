import pygame as pg
from global_values import *
import os

pg.init()
size=[size_hight,size_width]

# load main game textures
home_screen_png = pg.image.load(os.path.join("image","main_backgroubd.png"))
settings_screen_png = pg.image.load(os.path.join("image", "menu_ball.png"))
intermediate_menu_png = pg.image.load(os.path.join("image", "intermediate_menu.png"))

#loading background textures
texture_wood_png = pg.image.load(os.path.join("levels_image","texture_wood.jpg"))
texture_wood_1_png = pg.image.load(os.path.join("levels_image","texture_wood_1.png"))
texture_wood_2_png = pg.image.load(os.path.join("levels_image","texture_wood_2.png"))

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
go_back_png = pg.image.load(os.path.join("image", "go_back_down.png"))

dark_down_png = pg.image.load(os.path.join("image", "dark_down.png"))
disco_down_png = pg.image.load(os.path.join("image", "disco_down.png"))
grey_down_png = pg.image.load(os.path.join("image", "grey_down.png"))
red_down_png = pg.image.load(os.path.join("image", "red_down.png"))
striped_down_png = pg.image.load(os.path.join("image", "striped_down.png"))
magma_down_png = pg.image.load(os.path.join("image", "magma_down.png"))

arrow_down_png = pg.image.load(os.path.join("image", "arrow_down.png"))

cursor_up_png = pg.image.load(os.path.join("image", "cursor_up.png"))
cursor_down_png = pg.image.load(os.path.join("image", "cursor_down.png"))

#creating surfaces for objects 

#creating main sirfaace
home = pg.transform.scale(home_screen_png, size)
home_surface = pg.Surface(size, pg.SRCALPHA)
home_surface.blit(home, (0, 0))

menu_of_set = pg.transform.scale(settings_screen_png, size)
menu_of_set_surface = pg.Surface(size, pg.SRCALPHA)
menu_of_set_surface.blit(menu_of_set, (0, 0))

intermediate_menu = pg.transform.scale(intermediate_menu_png, size)
intermediate_menu_surface = pg.Surface(size, pg.SRCALPHA)
intermediate_menu_surface.blit(intermediate_menu, (0, 0))

#creating surface for main button

exitt = pg.transform.scale(exit_png, (281/1024*size_hight,93/576*size_width))
exit_surface = pg.Surface((281/1024*size_hight,93/576*size_width), pg.SRCALPHA)
exit_surface.blit(exitt, (0,0))

go = pg.transform.scale(go_png, (208/1024*size_hight,108/576*size_width))
go_surface = pg.Surface((208/1024*size_hight,108/576*size_width), pg.SRCALPHA)
go_surface.blit(go, (0,0))

settings = pg.transform.scale(settings_png, (320/1024*size_hight,107/576*size_width))
settings_surface = pg.Surface((320/1024*size_hight,107/576*size_width), pg.SRCALPHA)
settings_surface.blit(settings, (0,0))

nextlvl = pg.transform.scale(nextlvl_png, (440/1024*size_hight,140/576*size_width))
nextlvl_surface = pg.Surface((440/1024*size_hight,140/576*size_width), pg.SRCALPHA)
nextlvl_surface.blit(nextlvl, (0,0))

go_back = pg.transform.scale(go_back_png, (440/1024*size_hight,140/576*size_width))
go_back_surface = pg.Surface((440/1024*size_hight,140/576*size_width), pg.SRCALPHA)
go_back_surface.blit(go_back, (0,0))

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

#creating a button for an arrow

arrow_down = pg.transform.scale(arrow_down_png, (61/1024*size_hight,46/576*size_width))
arrow_button_surface = pg.Surface((61/1024*size_hight,46/576*size_width), pg.SRCALPHA)
arrow_button_surface.blit(arrow_down, (0,0))

cursor_up = pg.transform.scale(cursor_up_png, (cursor_size,cursor_size))
cursor_up_button_surface = pg.Surface((cursor_size,cursor_size), pg.SRCALPHA)
cursor_up_button_surface.blit(cursor_up, (0,0))

cursor_down = pg.transform.scale(cursor_down_png, (cursor_size,cursor_size))
cursor_down_button_surface = pg.Surface((cursor_size,cursor_size), pg.SRCALPHA)
cursor_down_button_surface.blit(cursor_down, (0,0))

#creating surface for balls

dark_ball = pg.transform.scale(dark_ball_png, (size_ball,size_ball))
dark_ball_surface = pg.Surface((size_ball,size_ball), pg.SRCALPHA)
dark_ball_surface.blit(dark_ball, (0,0))

disco_ball = pg.transform.scale(disco_ball_png, (size_ball,size_ball))
disco_ball_surface = pg.Surface((size_ball,size_ball), pg.SRCALPHA)
disco_ball_surface.blit(disco_ball, (0,0))

grey_ball = pg.transform.scale(grey_ball_png, (size_ball,size_ball))
grey_ball_surface = pg.Surface((size_ball,size_ball), pg.SRCALPHA)
grey_ball_surface.blit(grey_ball, (0,0))

red_ball = pg.transform.scale(red_ball_png, (size_ball,size_ball))
red_ball_surface = pg.Surface((size_ball,size_ball), pg.SRCALPHA)
red_ball_surface.blit(red_ball, (0,0))

striped_ball = pg.transform.scale(striped_ball_png, (size_ball,size_ball))
striped_ball_surface = pg.Surface((size_ball,size_ball), pg.SRCALPHA)
striped_ball_surface.blit(striped_ball, (0,0))

magma_ball = pg.transform.scale(magma_ball_png, (size_ball,size_ball))
magma_ball_surface = pg.Surface((size_ball,size_ball), pg.SRCALPHA)
magma_ball_surface.blit(magma_ball, (0,0))
