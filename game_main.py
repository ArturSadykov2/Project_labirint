from game_objects.game_menu import *
from game_levels.game_level_1 import level_1
from game_levels.game_level_2 import level_2
from game_levels.game_level_3 import level_3
from game_levels.game_level_4 import level_4
from game_colors import WHITE
from game_texture import *

pg.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512, devicename=None)
pg.init()

# set fps
FPS = 60

def main():
    """
    Function that draws main Menu with options of choose the level and starting the game
    """
    vjm_play = vile_jewish_sound.play(-1)
    rs_play = rolling_sound.play(-1)
    rs_play.pause()

    balls_surfaces = [red_ball_surface, grey_ball_surface, disco_ball_surface, dark_ball_surface, striped_ball_surface,
                      magma_ball_surface]
    screen = pg.display.set_mode(size)
    clock = pg.time.Clock()

    menu = Menu(screen)
    cursor = Cursor(screen)

    running = True
    pg.mouse.set_visible(False)

    while running:
        screen.fill(WHITE)
        clock.tick(FPS)

        for event in pg.event.get():
            if event.type == pg.QUIT or menu.exit_off:
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                cursor.click = True
                if menu.home_surface:
                    menu.check_on(event)
                elif menu.start_of_set:
                    menu.check_on_settings(event)
                elif menu.intermediate_menu or menu.pause_menu:
                    menu.check_on_game_windows(event)
            elif event.type == pg.MOUSEBUTTONUP:
                cursor.click = False
                if menu.home_surface:
                    menu.check_off()
                elif menu.start_of_set:
                    menu.check_off_settings()
                elif menu.intermediate_menu or menu.pause_menu:
                    menu.check_off_game_windows()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE and menu.pause_menu:
                    menu.continuee = True
            elif event.type == pg.KEYUP:
                if event.key == pg.K_SPACE and menu.pause_menu and menu.continuee:
                    menu.continuee = False
                    menu.pause_menu = 0
                    menu.menu_live = 0
            elif event.type == pg.MOUSEMOTION:
                cursor.cursor_change_pos(event)

        if menu.menu_live:
            menu.play_music(vjm_play)
            menu.screen_draw()
            menu.draw_bottons()
            menu.draw_bottons_balls()
        elif menu.level_1:
            vjm_play.pause()
            level_1([size_hight, size_width], balls_surfaces[menu.ball_index - 1], menu, rs_play)
            vjm_play.unpause()
            rs_play.pause()
        elif menu.level_2:
            vjm_play.pause()
            level_2([size_hight, size_width], balls_surfaces[menu.ball_index - 1], menu, balls_surfaces, rs_play)
            vjm_play.unpause()
            rs_play.pause()
        elif menu.level_3:
            vjm_play.pause()
            level_3([size_hight, size_width], balls_surfaces[menu.ball_index - 1], menu, balls_surfaces, rs_play)
            vjm_play.unpause()
            rs_play.pause()
        elif menu.level_4:
            vjm_play.pause()
            level_4([size_hight, size_width], balls_surfaces[menu.ball_index - 1], menu, balls_surfaces, rs_play)
            vjm_play.unpause()
            rs_play.pause()

        if menu.menu_live:
            cursor.draw_cursor()

        pg.display.flip()

    pg.quit()


if __name__ == "__main__":
    main()
