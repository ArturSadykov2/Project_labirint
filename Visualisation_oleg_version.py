import pygame as pg
import numpy as np
import os
from random import choice, randint
from game_menu import *
from game_colors import *
from global_values import *

size=[size_hight,size_width]

screen = pg.display.set_mode(size)
clock = pg.time.Clock()

menu=Menu(screen)
curs=Cursor(screen)

running = True
pg.mouse.set_visible(False)

while running:
    screen.fill(WHITE)
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT or menu.exit_off:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            print(event.pos[0],event.pos[1])
            if menu.home_surface:
                menu.check_on(event)
            elif menu.start_of_set:
                menu.check_on_settings(event)
        elif event.type == pg.MOUSEBUTTONUP:
            if menu.home_surface:
                menu.check_off()
            elif menu.start_of_set:
                menu.check_off_settings()
        elif event.type == pg.MOUSEMOTION:
            curs.cursor_change_pos(event)

    menu.main_screen_draw()
    menu.draw_bottons()
    menu.draw_bottons_balls()
    curs.draw_cursor()

    #pg.font.init()
    #pg.display.update()
    pg.display.flip()
pg.quit()
