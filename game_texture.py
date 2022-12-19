from global_values import *
import pygame as pg
import os

# load main game textures
home_screen_png = pg.image.load(os.path.join("image", "main_backgroubd.png"))
settings_screen_png = pg.image.load(os.path.join("image", "menu_ball.png"))
intermediate_menu_png = pg.image.load(os.path.join("image", "intermediate_menu.png"))
pause_menu_png = pg.image.load(os.path.join("image", "pause_menu.png"))

# loading background textures
texture_wood_png = pg.image.load(os.path.join("image", "levels_image", "texture_wood.jpg"))
texture_wood_1_png = pg.image.load(os.path.join("image", "levels_image", "texture_wood_1.png"))
texture_wood_2_png = pg.image.load(os.path.join("image", "levels_image", "texture_wood_2.png"))

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
continue_png = pg.image.load(os.path.join("image", "continue_down.png"))

dark_down_png = pg.image.load(os.path.join("image", "dark_down.png"))
disco_down_png = pg.image.load(os.path.join("image", "disco_down.png"))
grey_down_png = pg.image.load(os.path.join("image", "grey_down.png"))
red_down_png = pg.image.load(os.path.join("image", "red_down.png"))
striped_down_png = pg.image.load(os.path.join("image", "striped_down.png"))
magma_down_png = pg.image.load(os.path.join("image", "magma_down.png"))

arrow_down_png = pg.image.load(os.path.join("image", "arrow_down.png"))

cursor_up_png = pg.image.load(os.path.join("image", "cursor_up.png"))
cursor_down_png = pg.image.load(os.path.join("image", "cursor_down.png"))

# creating surfaces for objects

# creating main surface

home = pg.transform.scale(home_screen_png, size)
home_surface = pg.Surface(size, pg.SRCALPHA)
home_surface.blit(home, (0, 0))

menu_of_set = pg.transform.scale(settings_screen_png, size)
menu_of_set_surface = pg.Surface(size, pg.SRCALPHA)
menu_of_set_surface.blit(menu_of_set, (0, 0))

intermediate_menu = pg.transform.scale(intermediate_menu_png, size)
intermediate_menu_surface = pg.Surface(size, pg.SRCALPHA)
intermediate_menu_surface.blit(intermediate_menu, (0, 0))

pause_menu = pg.transform.scale(pause_menu_png, size)
pause_menu_surface = pg.Surface(size, pg.SRCALPHA)
pause_menu_surface.blit(pause_menu, (0, 0))

# creating surface for main button

exitt = pg.transform.scale(exit_png, (281 * scale_x, 93 * scale_y))
exit_surface = pg.Surface((281 * scale_x, 93 * scale_y), pg.SRCALPHA)
exit_surface.blit(exitt, (0, 0))

go = pg.transform.scale(go_png, (208 * scale_x, 108 * scale_y))
go_surface = pg.Surface((208 * scale_x, 108 * scale_y), pg.SRCALPHA)
go_surface.blit(go, (0, 0))

settings = pg.transform.scale(settings_png, (320 * scale_x, 107 * scale_y))
settings_surface = pg.Surface((320 * scale_x, 107 * scale_y), pg.SRCALPHA)
settings_surface.blit(settings, (0, 0))

nextlvl = pg.transform.scale(nextlvl_png, (440 * scale_x, 140 * scale_y))
nextlvl_surface = pg.Surface((440 * scale_x, 140 * scale_y), pg.SRCALPHA)
nextlvl_surface.blit(nextlvl, (0, 0))

go_back = pg.transform.scale(go_back_png, (440 * scale_x, 140 * scale_y))
go_back_surface = pg.Surface((440 * scale_x, 140 * scale_y), pg.SRCALPHA)
go_back_surface.blit(go_back, (0, 0))

continuee = pg.transform.scale(continue_png, (440 * scale_x, 140 * scale_y))
continue_surface = pg.Surface((440 * scale_x, 140 * scale_y), pg.SRCALPHA)
continue_surface.blit(continuee, (0, 0))

# creating buttons for selecting balls

dark_down = pg.transform.scale(dark_down_png, (215 * scale_x, 215 * scale_y))
dark_button_surface = pg.Surface((215 * scale_x, 215 * scale_y), pg.SRCALPHA)
dark_button_surface.blit(dark_down, (0, 0))

disco_down = pg.transform.scale(disco_down_png, (215 * scale_x, 215 * scale_y))
disco_button_surface = pg.Surface((215 * scale_x, 215 * scale_y), pg.SRCALPHA)
disco_button_surface.blit(disco_down, (0, 0))

grey_down = pg.transform.scale(grey_down_png, (215 * scale_x, 215 * scale_y))
grey_button_surface = pg.Surface((215 * scale_x, 215 * scale_y), pg.SRCALPHA)
grey_button_surface.blit(grey_down, (0, 0))

red_down = pg.transform.scale(red_down_png, (215 * scale_x, 215 * scale_y))
red_button_surface = pg.Surface((215 * scale_x, 215 * scale_y), pg.SRCALPHA)
red_button_surface.blit(red_down, (0, 0))

striped_down = pg.transform.scale(striped_down_png, (215 * scale_x, 215 * scale_y))
striped_button_surface = pg.Surface((215 * scale_x, 215 * scale_y), pg.SRCALPHA)
striped_button_surface.blit(striped_down, (0, 0))

magma_down = pg.transform.scale(magma_down_png, (215 * scale_x, 215 * scale_y))
magma_button_surface = pg.Surface((215 * scale_x, 215 * scale_y), pg.SRCALPHA)
magma_button_surface.blit(magma_down, (0, 0))

# creating a button for an arrow

arrow_down = pg.transform.scale(arrow_down_png, (61 * scale_x, 46 * scale_y))
arrow_button_surface = pg.Surface((61 * scale_x, 46 * scale_y), pg.SRCALPHA)
arrow_button_surface.blit(arrow_down, (0, 0))

cursor_up = pg.transform.scale(cursor_up_png, (cursor_size, cursor_size))
cursor_up_button_surface = pg.Surface((cursor_size, cursor_size), pg.SRCALPHA)
cursor_up_button_surface.blit(cursor_up, (0, 0))

cursor_down = pg.transform.scale(cursor_down_png, (cursor_size, cursor_size))
cursor_down_button_surface = pg.Surface((cursor_size, cursor_size), pg.SRCALPHA)
cursor_down_button_surface.blit(cursor_down, (0, 0))

# creating surface for balls

dark_ball = pg.transform.scale(dark_ball_png, size_ball)
dark_ball_surface = pg.Surface(size_ball, pg.SRCALPHA)
dark_ball_surface.blit(dark_ball, (0, 0))

disco_ball = pg.transform.scale(disco_ball_png, size_ball)
disco_ball_surface = pg.Surface(size_ball, pg.SRCALPHA)
disco_ball_surface.blit(disco_ball, (0, 0))

grey_ball = pg.transform.scale(grey_ball_png, size_ball)
grey_ball_surface = pg.Surface(size_ball, pg.SRCALPHA)
grey_ball_surface.blit(grey_ball, (0, 0))

red_ball = pg.transform.scale(red_ball_png, size_ball)
red_ball_surface = pg.Surface(size_ball, pg.SRCALPHA)
red_ball_surface.blit(red_ball, (0, 0))

striped_ball = pg.transform.scale(striped_ball_png, size_ball)
striped_ball_surface = pg.Surface(size_ball, pg.SRCALPHA)
striped_ball_surface.blit(striped_ball, (0, 0))

magma_ball = pg.transform.scale(magma_ball_png, size_ball)
magma_ball_surface = pg.Surface(size_ball, pg.SRCALPHA)
magma_ball_surface.blit(magma_ball, (0, 0))

#the texture of the levels

bullet_mask = pg.mask.from_surface(dark_ball_surface)

karusel_floor = pg.image.load(os.path.join("image", "levels_image", "karysel3.png"))
karusel_floor = pg.transform.scale(karusel_floor, disk_size)
disk_floor_surf = pg.Surface(disk_size, pg.SRCALPHA)
disk_floor_surf.blit(karusel_floor, (0, 0))
disk_floor_mask = pg.mask.from_surface(disk_floor_surf)

karusel_walls = pg.image.load(os.path.join("image", "levels_image", "karysel_walls.png"))
karusel_walls = pg.transform.scale(karusel_walls, disk_size)
disk_walls_surf = pg.Surface(disk_size, pg.SRCALPHA)
disk_walls_surf.blit(karusel_walls, (0, 0))
disk_wall_mask = pg.mask.from_surface(disk_walls_surf)

texture_wood_png = pg.image.load(os.path.join("image", "levels_image", "texture_wood.jpg"))
texture_wood_png = pg.transform.scale(texture_wood_png, size)
bg_wood_surface = pg.Surface(size, pg.SRCALPHA)
bg_wood_surface.blit(texture_wood_png, (0, 0))

lv1_light = pg.image.load(os.path.join("image", "levels_image", "level_1", "lv1_sp_light.png"))
lv1_light = pg.transform.scale(lv1_light, size)
lv1_walls_surf = pg.Surface(size, pg.SRCALPHA)
lv1_walls_surf.blit(lv1_light, (0, 0))

lv1_dark = pg.image.load(os.path.join("image", "levels_image", "level_1", "lv1_super_dark.png"))
lv1_dark = pg.transform.scale(lv1_dark, size)
lv1_dark_surf = pg.Surface(size, pg.SRCALPHA)
lv1_dark_surf.blit(lv1_dark, (0, 0))

lv1_traps = pg.image.load(os.path.join("image", "levels_image", "level_1", "lv1_lovushka_2.png"))
lv1_traps = pg.transform.scale(lv1_traps, size)
lv1_traps_surf = pg.Surface(size, pg.SRCALPHA)
lv1_traps_surf.blit(lv1_traps, (0, 0))

finish_texture = pg.image.load(os.path.join("image", "levels_image", "final_hole.png"))
finish_texture = pg.transform.scale(finish_texture, [finish_width, finish_hight])
finish_surf = pg.Surface([finish_width, finish_hight], pg.SRCALPHA)
finish_surf.blit(finish_texture, (0, 0))

lv2_walls = pg.image.load(os.path.join("image", "levels_image", "level_2", "lv2_bw.png"))
lv2_walls = pg.transform.scale(lv2_walls, size)
lv2_walls_surf = pg.Surface(size, pg.SRCALPHA)
lv2_walls_surf.blit(lv2_walls, (0, 0))

lv2_traps = pg.image.load(os.path.join("image", "levels_image", "level_2", "lv2_lovyshka.png"))
lv2_traps = pg.transform.scale(lv2_traps, size)
lv2_traps_surf = pg.Surface(size, pg.SRCALPHA)
lv2_traps_surf.blit(lv2_traps, (0, 0))

lv2_dark = pg.image.load(os.path.join("image", "levels_image", "level_2", "lv2_without_guns.png"))
lv2_dark = pg.transform.scale(lv2_dark, size)
lv2_dark_surf = pg.Surface(size, pg.SRCALPHA)
lv2_dark_surf.blit(lv2_dark, (0, 0))

lv3_walls = pg.image.load(os.path.join("image", "levels_image", "level_3", "lv3_light.png"))
lv3_walls = pg.transform.scale(lv3_walls, size)
lv3_walls_surf = pg.Surface(size, pg.SRCALPHA)
lv3_walls_surf.blit(lv3_walls, (0, 0))

lv3_traps = pg.image.load(os.path.join("image", "levels_image", "level_3", "lv3_lovyshki_dark.png"))
lv3_traps = pg.transform.scale(lv3_traps, size)
lv3_traps_surf = pg.Surface(size, pg.SRCALPHA)
lv3_traps_surf.blit(lv3_traps, (0, 0))

lv3_dark = pg.image.load(os.path.join("image", "levels_image", "level_3", "lv3_without_guns.png"))
lv3_dark = pg.transform.scale(lv3_dark, size)
lv3_dark_surf = pg.Surface(size, pg.SRCALPHA)
lv3_dark_surf.blit(lv3_dark, (0, 0))

lv4_walls_g = pg.image.load(os.path.join("image", "levels_image", "level_4", "lv4_without_guns.png"))
lv4_walls_g = pg.transform.scale(lv4_walls_g, size)
lv4_walls_surf_g = pg.Surface(size, pg.SRCALPHA)
lv4_walls_surf_g.blit(lv4_walls_g, (0, 0))

lv4_walls = pg.image.load(os.path.join("image", "levels_image", "level_4", "lv4_light.png"))
lv4_walls = pg.transform.scale(lv4_walls, size)
lv4_walls_surf = pg.Surface(size, pg.SRCALPHA)
lv4_walls_surf.blit(lv4_walls, (0, 0))

lv4_traps = pg.image.load(os.path.join("image", "levels_image", "level_4", "lv4_lovyshki_dark.png"))
lv4_traps = pg.transform.scale(lv4_traps, size)
lv4_traps_surf = pg.Surface(size, pg.SRCALPHA)
lv4_traps_surf.blit(lv4_traps, (0, 0))

lv4_dark = pg.image.load(os.path.join("image", "levels_image", "level_4", "lv4_dark.png"))
lv4_dark = pg.transform.scale(lv4_dark, size)
lv4_dark_surf = pg.Surface(size, pg.SRCALPHA)
lv4_dark_surf.blit(lv4_dark, (0, 0))
