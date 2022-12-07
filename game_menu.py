import pygame as pg
import numpy as np
from global_values import *
from game_texture_oleg import *
from game_texture_Artur import *
import os

pg.init()
size=[size_hight,size_width]

class Menu:
    '''
    Function that draws main Menu with options of choose the level and starting the game
    '''
    def __init__(self,screen):
        self.home_surface = 1
        self.start_of_set = 0
        self.screen = screen
        self.exit_on=False
        self.exit_off=False
        self.go=False
        self.settings=False
        self.nextlvl=False
        self.dark_button=False
        self.disco_button=False
        self.grey_button=False
        self.red_button=False
        self.striped_button=False
        self.magma_button=False
        self.arrow_button=False

    def check_on(self, event):
        if (0<=event.pos[0]-131/1024*size_hight<=281/1024*size_hight) and (0<=event.pos[1]-153/576*size_width<=92/576*size_width):
            self.exit_on=True
        elif (0<=event.pos[0]-671/1024*size_hight<=206/1024*size_hight) and (0<=event.pos[1]-153/576*size_width<=107/576*size_width):
            self.go=True
        elif (0<=event.pos[0]-272/1024*size_hight<=320/1024*size_hight) and (0<=event.pos[1]-394/576*size_width<=106/576*size_width):
            self.settings=True
        elif (0<=event.pos[0]-671/1024*size_hight<=206/1024*size_hight) and (0<=event.pos[1]-153/576*size_width<=107/576*size_width):
            pass
            #self.nextlvl=True

    def check_on_settings(self,event):
        if (0<=event.pos[0]-721/1024*size_hight<=215/1024*size_hight) and (0<=event.pos[1]-50/576*size_width<=215/576*size_width):
            self.dark_button=True
        elif (0<=event.pos[0]-74/1024*size_hight<=215/1024*size_hight) and (0<=event.pos[1]-320/576*size_width<=215/576*size_width):
            self.disco_button=True
        elif (0<=event.pos[0]-74/1024*size_hight<=215/1024*size_hight) and (0<=event.pos[1]-50/576*size_width<=215/576*size_width):
            self.grey_button=True
        elif (0<=event.pos[0]-399/1024*size_hight<=215/1024*size_hight) and (0<=event.pos[1]-50/576*size_width<=215/576*size_width):
            self.red_button=True
        elif (0<=event.pos[0]-399/1024*size_hight<=215/1024*size_hight) and (0<=event.pos[1]-320/576*size_width<=215/576*size_width):
            self.striped_button=True
        elif (0<=event.pos[0]-721/1024*size_hight<=215/1024*size_hight) and (0<=event.pos[1]-320/576*size_width<=215/576*size_width):
            self.magma_button=True
        elif (0<=event.pos[0]<=61/1024*size_hight) and (0<=event.pos[1]<=46/576*size_width):
            self.arrow_button=True
        

    def check_off(self):
        if self.exit_on:
            self.exit_off=True
            self.exit_on=False
        elif self.go:
            self.go=False
        elif self.settings:
            self.settings=False
            self.start_of_set=1
            self.home_surface=0
        elif self.nextlvl:
            self.nextlvl=False

    def check_off_settings(self):
        if self.arrow_button:
            self.arrow_button = False
            self.start_of_set=0
            self.home_surface=1
        elif self.dark_button:
            self.dark_button=False
        elif self.disco_button:
            self.disco_button=False
        elif self.grey_button:
            self.grey_button=False
        elif self.red_button:
            self.red_button=False
        elif self.striped_button:
            self.striped_button=False
        elif self.magma_button:
            self.magma_button=False

    def draw_bottons(self):
        if self.exit_on:
            self.screen.blit(exit_surface, (131/1024*size_hight, 153/576*size_width))
        elif self.go:
            self.screen.blit(go_surface, (672/1024*size_hight, 153/576*size_width))
        elif self.nextlvl:
            #self.screen.blit(nextlvl_surface, (131/1024*size_hight, 153/576*size_width))
            pass
        elif self.settings:
            self.screen.blit(settings_surface, (272/1024*size_hight, 394/576*size_width))
    
    def draw_bottons_balls(self):
        if self.dark_button:
            self.screen.blit(dark_button_surface, (721/1024*size_hight, 50/576*size_width))
        elif self.disco_button:
            self.screen.blit(disco_button_surface, (74/1024*size_hight, 320/576*size_width))
        elif self.grey_button:
            self.screen.blit(grey_button_surface, (74/1024*size_hight, 50/576*size_width))
        elif self.red_button:
            self.screen.blit(red_button_surface, (399/1024*size_hight, 50/576*size_width))
        elif self.striped_button:
            self.screen.blit(striped_button_surface, (399/1024*size_hight, 320/576*size_width))
        elif self.magma_button:
            self.screen.blit(magma_button_surface, (721/1024*size_hight, 320/576*size_width))
        elif self.arrow_button:
            self.screen.blit(arrow_button_surface, (0,0))

    def main_screen_draw(self):
        if self.start_of_set:
            self.screen.blit(menu_of_set_surface, (0,0))
        elif self.home_surface:
            self.screen.blit(home_surface, (0, 0))

            

class Cursor:
    def __init__(self, screen, x = 0, y = 0):
        self.screen = screen
        self.y = y
        self.x = x

    def cursor_change_pos(self, event):
        self.x,self.y=event.pos[0],event.pos[1]

    def draw_cursor(self, r = 10, Crimson=[220, 20, 60], BLACK=(0,0,0)):
        center=np.array([self.x,self.y])
        pg.draw.circle(self.screen, Crimson, center, r, round(r/5))
        pg.draw.circle(self.screen, BLACK, center, 2)

        p1,p2=np.array([r/2,0])+center, np.array([1.5*r,0])+center
        pg.draw.line(self.screen, Crimson, p1, p2, 3)

        c1,c2=np.array([-r/2,0])+center, np.array([-1.5*r,0])+center
        pg.draw.line(self.screen, Crimson, c1, c2, 3)

        b1,b2=np.array([0,r/2])+center, np.array([0,1.5*r])+center
        pg.draw.line(self.screen, Crimson, b1, b2, 3)

        d1,d2=np.array([0,-r/2])+center, np.array([0,-1.5*r])+center
        pg.draw.line(self.screen, Crimson, d1, d2, 3)