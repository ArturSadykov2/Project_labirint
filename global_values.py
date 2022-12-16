import numpy as np
import pygame as pg
pg.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512, devicename=None)
pg.init()

size_hight=1392
size_width=783
scale_x=size_hight/1024
scale_y=size_width/576

# set screen size
size = np.array([size_hight, size_width])

# set start coordinate
coord_of_start = np.array([[90,80],[100,80],[1250,75],[100,360]])

vile_jewish_music=pg.mixer.Sound("music/vile_jewish_music.wav")
rolling_sound=pg.mixer.Sound("music/rolling_sound.wav")
bounce_sound=pg.mixer.Sound("music/bounce_sound.wav")

size_ball=np.array([50*scale_x, 50*scale_x])
cursor_size=100*scale_x
finish_hight = 50*scale_x
finish_width = 100*scale_x
disk_size = np.array([480*scale_x, 480*scale_x])
