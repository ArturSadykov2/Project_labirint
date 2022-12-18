from game_texture import *

class Menu:
    """
    Сlass Menu is used for setting up and starting the game, as well as drawing the menu
    """

    def __init__(self, screen):
        """
        Sets the basic parameters of menu
        :param screen: current drawing screen
        """
        self.ball_index = 1
        self.menu_live = 1
        self.screen = screen
        self.home_surface = 1
        self.start_of_set = 0
        self.intermediate_menu = 0
        self.pause_menu = 0
        self.exit_on = False
        self.exit_off = False
        self.go = False
        self.settings = False
        self.nextlvl = False
        self.go_back = False
        self.continuee = False
        self.dark_button = False
        self.disco_button = False
        self.grey_button = False
        self.red_button = False
        self.striped_button = False
        self.magma_button = False
        self.arrow_button = False
        self.level_1 = 1
        self.level_2 = 0
        self.level_3 = 0
        self.level_4 = 0

    def check_on(self, event):
        """
        registers the keystroke and changes the menu options depending on the keys pressed
        :param event: an iterable object with the coordinates of the point where the key was pressed
        :return: nothing
        """
        if (0 <= event.pos[0] - 131 * scale_x + cursor_size / 2 <= 281 * scale_x) and (
                0 <= event.pos[1] - 153 * scale_y + cursor_size / 2 <= 92 * scale_y):
            self.exit_on = True
        elif (0 <= event.pos[0] - 671 * scale_x + cursor_size / 2 <= 206 * scale_x) and (
                0 <= event.pos[1] - 153 * scale_y + cursor_size / 2 <= 107 * scale_y):
            self.go = True
        elif (0 <= event.pos[0] - 272 * scale_x + cursor_size / 2 <= 320 * scale_x) and (
                0 <= event.pos[1] - 394 * scale_y + cursor_size / 2 <= 106 * scale_y):
            self.settings = True

    def check_on_settings(self, event):
        """
        registers the keystroke and changes the menu options depending
        on the keys pressed in the settings menu
        :param event: an iterable object with the coordinates of the point where the key was pressed
        :return: nothing
        """
        if (0 <= event.pos[0] - 721 * scale_x + cursor_size / 2 <= 215 * scale_x) and (
                0 <= event.pos[1] - 50 * scale_y + cursor_size / 2 <= 215 * scale_y):
            self.dark_button = True
            self.ball_index = 4
        elif (0 <= event.pos[0] - 74 * scale_x + cursor_size / 2 <= 215 * scale_x) and (
                0 <= event.pos[1] - 320 * scale_y + cursor_size / 2 <= 215 * scale_y):
            self.disco_button = True
            self.ball_index = 3
        elif (0 <= event.pos[0] - 74 * scale_x + cursor_size / 2 <= 215 * scale_x) and (
                0 <= event.pos[1] - 50 * scale_y + cursor_size / 2 <= 215 * scale_y):
            self.grey_button = True
            self.ball_index = 2
        elif (0 <= event.pos[0] - 399 * scale_x + cursor_size / 2 <= 215 * scale_x) and (
                0 <= event.pos[1] - 50 * scale_y + cursor_size / 2 <= 215 * scale_y):
            self.red_button = True
            self.ball_index = 1
        elif (0 <= event.pos[0] - 399 * scale_x + cursor_size / 2 <= 215 * scale_x) and (
                0 <= event.pos[1] - 320 * scale_y + cursor_size / 2 <= 215 * scale_y):
            self.striped_button = True
            self.ball_index = 5
        elif (0 <= event.pos[0] - 721 * scale_x + cursor_size / 2 <= 215 * scale_x) and (
                0 <= event.pos[1] - 320 * scale_y + cursor_size / 2 <= 215 * scale_y):
            self.magma_button = True
            self.ball_index = 6
        elif (0 <= event.pos[0] <= 61 * scale_x) and (0 <= event.pos[1] <= 46 * scale_y):
            self.arrow_button = True

    def check_on_game_windows(self, event):
        """
        registers the keystroke and changes the menu options depending on the keys pressed
        in the menu modes after the start of the game
        :param event: an iterable object with the coordinates of the point where the key was pressed
        :return: nothing 
        """
        if (0 <= event.pos[0] - 292 * scale_x + cursor_size / 2 <= 440 * scale_x) and (
                0 <= event.pos[1] - 332 * scale_y + cursor_size / 2 <= 140 * scale_y):
            self.go_back = True
        elif (0 <= event.pos[0] - 292 * scale_x + cursor_size / 2 <= 440 * scale_x) and (
                0 <= event.pos[1] - 128 * scale_y + cursor_size / 2 <= 140 * scale_y) and self.intermediate_menu:
            self.nextlvl = True
        elif (0 <= event.pos[0] - 292 * scale_x + cursor_size / 2 <= 440 * scale_x) and (
                0 <= event.pos[1] - 128 * scale_y + cursor_size / 2 <= 140 * scale_y) and self.pause_menu:
            self.continuee = True

    def check_off(self):
        """
        Changes the menu options depending on the released keys
        :return: nothing
        """
        if self.exit_on:
            self.exit_off = True
            self.exit_on = False
        elif self.go:
            self.go = False
            self.menu_live = 0
            self.home_surface = 0
        elif self.settings:
            self.settings = False
            self.start_of_set = 1
            self.home_surface = 0

    def check_off_settings(self):
        """
        Changes the menu options depending on the released keys in the settings menu
        :return: nothing
        """
        if self.arrow_button:
            self.arrow_button = False
            self.start_of_set = 0
            self.home_surface = 1
        elif self.dark_button:
            self.dark_button = False
        elif self.disco_button:
            self.disco_button = False
        elif self.grey_button:
            self.grey_button = False
        elif self.red_button:
            self.red_button = False
        elif self.striped_button:
            self.striped_button = False
        elif self.magma_button:
            self.magma_button = False

    def check_off_game_windows(self):
        """
        Changes the menu options depending on the released keys
        in the menu modes after the start of the game
        :return: nothing
        """
        if self.go_back:
            self.go_back = False
            self.home_surface = 1
            self.intermediate_menu = 0
            self.pause_menu = 0
        elif self.nextlvl:
            self.nextlvl = False
            self.menu_live = 0
            if self.level_1:
                self.level_2 = 1
                self.level_1 = 0
            elif self.level_2:
                self.level_3 = 1
                self.level_2 = 0
            elif self.level_3:
                self.level_4 = 1
                self.level_3 = 0
        elif self.continuee:
            self.continuee = False
            self.pause_menu = 0
            self.menu_live = 0

    def draw_bottons(self):
        """
        Draws animation of pressing buttons
        :return: nothing
        """
        if self.exit_on:
            self.screen.blit(exit_surface, (131 * scale_x, 153 * scale_y))
        elif self.go:
            self.screen.blit(go_surface, (672 * scale_x, 153 * scale_y))
        elif self.nextlvl:
            self.screen.blit(nextlvl_surface, (292 * scale_x, 128 * scale_y))
        elif self.settings:
            self.screen.blit(settings_surface, (272 * scale_x, 394 * scale_y))
        elif self.go_back:
            self.screen.blit(go_back_surface, (292 * scale_x, 332 * scale_y))
        elif self.continuee:
            self.screen.blit(continue_surface, (292 * scale_x, 128 * scale_y))

    def draw_bottons_balls(self):
        """
        Draws animation of pressing buttons when selecting balls in the settings menu
        :return: nothing
        """
        if self.dark_button:
            self.screen.blit(dark_button_surface, (721 * scale_x, 50 * scale_y))
        elif self.disco_button:
            self.screen.blit(disco_button_surface, (74 * scale_x, 320 * scale_y))
        elif self.grey_button:
            self.screen.blit(grey_button_surface, (74 * scale_x, 50 * scale_y))
        elif self.red_button:
            self.screen.blit(red_button_surface, (399 * scale_x, 50 * scale_y))
        elif self.striped_button:
            self.screen.blit(striped_button_surface, (399 * scale_x, 320 * scale_y))
        elif self.magma_button:
            self.screen.blit(magma_button_surface, (721 * scale_x, 320 * scale_y))
        elif self.arrow_button:
            self.screen.blit(arrow_button_surface, (0, 0))

    def screen_draw(self):
        """
        Draws the background for the main menu modes
        :return: nothing
        """
        if self.start_of_set:
            self.screen.blit(menu_of_set_surface, (0, 0))
        elif self.home_surface:
            self.screen.blit(home_surface, (0, 0))
        elif self.intermediate_menu:
            self.screen.blit(intermediate_menu_surface, (0, 0))
        elif self.pause_menu:
            self.screen.blit(pause_menu_surface, (0, 0))

    def play_music(self, channel):
        if self.intermediate_menu:
            channel.pause()
        elif self.pause_menu:
            channel.pause()
        else:
            channel.unpause()


class Cursor:
    """
    Class Cursor is used to change the appearance of the cursor
    """

    def __init__(self, screen, x=0, y=0):
        """
        Sets the basic parameters of cursor
        :param screen: current drawing screen
        """
        self.screen = screen
        self.click = False
        self.y = y
        self.x = x

    def cursor_change_pos(self, event):
        """
        Changes the cursor coordinates to the actual ones when moving
        :param event: an iterable object with the coordinates of the current cursor position
        :return: nothing
        """
        self.x, self.y = event.pos[0], event.pos[1]

    def draw_cursor(self):
        """
        Draws the cursor image
        :return: nothing
        """
        if self.click:
            self.screen.blit(cursor_down_button_surface, (self.x, self.y))
        else:
            self.screen.blit(cursor_up_button_surface, (self.x, self.y))
