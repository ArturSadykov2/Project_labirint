import pygame as pg
import numpy as np
from game_menu import *
from game_colors import *
from global_values import *
from game_texture_oleg import *
from game_levels import *

#set fps
FPS = 60

#set screen size
size=[size_hight,size_width]

def main():
    '''
    Function that draws main Menu with options of choose the level and starting the game
    '''
    balls_surfaces=[red_ball_surface,disco_ball_surface,grey_ball_surface,dark_ball_surface,striped_ball_surface,magma_ball_surface]
    screen = pg.display.set_mode(size)
    clock = pg.time.Clock()

    menu=Menu(screen)
    cursor=Cursor(screen)

    running = True
    pg.mouse.set_visible(False)

    while running:
        screen.fill(WHITE)
        clock.tick(FPS)

        for event in pg.event.get():
            if event.type == pg.QUIT or menu.exit_off:
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                print(event.pos[0],event.pos[1])
                cursor.click=True
                if menu.home_surface:
                    menu.check_on(event)
                elif menu.start_of_set:
                    menu.check_on_settings(event)
                elif menu.intermediate_menu:
                    menu.check_on_intermediate(event)
            elif event.type == pg.MOUSEBUTTONUP:
                cursor.click=False
                if menu.home_surface:
                    menu.check_off()
                elif menu.start_of_set:
                    menu.check_off_settings()
                elif menu.intermediate_menu:
                    menu.check_off_intermediate()
            elif event.type == pg.MOUSEMOTION:
                cursor.cursor_change_pos(event)

        if menu.menu_live:
            menu.main_screen_draw()
            menu.draw_bottons()
            menu.draw_bottons_balls()
        elif menu.level_1:
            level_1([size_hight, size_width], balls_surfaces[menu.ball_index-1])



        cursor.draw_cursor()
        #pg.font.init()
        #pg.display.update()
        pg.display.flip()
        
    pg.quit()

if __name__ == "__main__":
    main()