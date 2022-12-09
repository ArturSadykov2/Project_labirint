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

# start coordinates
x1 = 80
y1 = 100
x2 = 100
y2 = 100
x3 = 200
y3 = 100
x4 = 150
y4 = size_hight//2

# finish coordinates
xf1 = 1200
yf1 = 600
xf2 = 1300
yf2 = 700
xf3 = 1300
yf3 = 700
xf4 = 1300
yf4 = 700

# level texture massive
level_texture = [[lv1_walls_surf, lv1_traps_surf, x1, y1, xf1, yf1],
                 [lv2_walls_surf, lv2_traps_surf, x2, y2, xf2, yf2],
                 [lv3_walls_surf, lv3_traps_surf, x3, y3, xf3, yf3],
                 [lv4_walls_surf, lv4_traps_surf, x4, y4, xf4, yf4]]
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
            level([size_hight, size_width], balls_surfaces[menu.ball_index-1],
                  level_texture[0][0], level_texture[0][1],
                  level_texture[0][2], level_texture[0][3],
                  level_texture[0][4], level_texture[0][5],
                  menu)
        elif menu.level_2:
            level([size_hight, size_width], balls_surfaces[menu.ball_index-1],
                  level_texture[1][0], level_texture[1][1],
                  level_texture[1][2], level_texture[1][3],
                  level_texture[1][4], level_texture[1][5],
                  menu)
        elif menu.level_3:
            level([size_hight, size_width], balls_surfaces[menu.ball_index-1],
                  level_texture[2][0], level_texture[2][1],
                  level_texture[2][2], level_texture[2][3],
                  level_texture[2][4], level_texture[2][5],
                  menu)
        elif menu.level_4:
            level([size_hight, size_width], balls_surfaces[menu.ball_index-1],
                  level_texture[3][0], level_texture[3][1],
                  level_texture[3][2], level_texture[3][3],
                  level_texture[3][4], level_texture[3][5],
                  menu)




        cursor.draw_cursor()
        #pg.font.init()
        #pg.display.update()
        pg.display.flip()
        
    pg.quit()

if __name__ == "__main__":
    main()
