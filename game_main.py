import pygame as pg
import numpy as np
from game_menu import *
from game_colors import *
from global_values import *
from game_texture_oleg import *
from game_levels import *
from game_level_1 import level_1
from game_level_2 import level_2
from game_level_3 import level_3
from game_level_4 import level_4

#set fps
FPS = 60

#set screen size
size=[size_hight,size_width]

# start coordinates
x1 = 80
y1 = 500
x2 = 500
y2 = 300
x3 = 200
y3 = 100
x4 = 100
y4 = size_width//2

# finish coordinates
xf1 = 80
yf1 = 600
xf2 = 1050
yf2 = 650
xf3 = 1300
yf3 = 700
xf4 = 100
yf4 = size_width//2

# level texture massive
level_texture = [[lv1_walls_surf, lv1_traps_surf, lv1_dark_surf, x1, y1, xf1, yf1],
                 [lv2_walls_surf, lv2_traps_surf, lv2_dark_surf, x2, y2, xf2, yf2],
                 [lv3_walls_surf, lv3_traps_surf, lv3_dark_surf, x3, y3, xf3, yf3],
                 [lv4_walls_surf, lv4_traps_surf, lv4_dark_surf, x4, y4, xf4, yf4]]
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
            menu.screen_draw()
            menu.draw_bottons()
            menu.draw_bottons_balls()
        elif menu.level_1:
            level_1([size_hight, size_width], balls_surfaces[menu.ball_index-1], menu)
        elif menu.level_2:
            level_2([size_hight, size_width], balls_surfaces[menu.ball_index-1], menu)
        elif menu.level_3:
            level_3([size_hight, size_width], balls_surfaces[menu.ball_index-1], menu)
        elif menu.level_4:
            level_4([size_hight, size_width], balls_surfaces[menu.ball_index-1], menu)




        cursor.draw_cursor()
        #pg.font.init()
        #pg.display.update()
        pg.display.flip()
        
    pg.quit()

if __name__ == "__main__":
    main()
