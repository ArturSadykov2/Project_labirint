from game_texture_oleg import *
from global_values import *

bullet_mask = pg.mask.from_surface(dark_ball_surface)

karusel_floor = pg.image.load(os.path.join("levels_image", "karysel3.png"))
karusel_floor = pg.transform.scale(karusel_floor, disk_size)
disk_floor_surf = pg.Surface(disk_size, pg.SRCALPHA)
disk_floor_surf.blit(karusel_floor, (0, 0))
disk_floor_mask = pg.mask.from_surface(disk_floor_surf)
karusel_walls = pg.image.load(os.path.join("levels_image", "karysel_walls.png"))
karusel_walls = pg.transform.scale(karusel_walls, disk_size)
disk_walls_surf = pg.Surface(disk_size, pg.SRCALPHA)
disk_walls_surf.blit(karusel_walls, (0, 0))
disk_wall_mask = pg.mask.from_surface(disk_walls_surf)

texture_wood_png = pg.image.load(os.path.join("levels_image", "texture_wood.jpg"))
texture_wood_png = pg.transform.scale(texture_wood_png, size)
bg_wood_surface = pg.Surface(size, pg.SRCALPHA)
bg_wood_surface.blit(texture_wood_png, (0, 0))

texture_red_png = pg.image.load(os.path.join("levels_image", "red_background.jpg"))
texture_red_png = pg.transform.scale(texture_red_png, size)
bg_red_surface = pg.Surface(size, pg.SRCALPHA)
bg_red_surface.blit(texture_red_png, (0, 0))

lv1_light = pg.image.load(os.path.join("levels_image", "level_1", "lv1_sp_light.png"))
lv1_light = pg.transform.scale(lv1_light, size)
lv1_walls_surf = pg.Surface(size, pg.SRCALPHA)
lv1_walls_surf.blit(lv1_light, (0, 0))

lv1_dark = pg.image.load(os.path.join("levels_image", "level_1", "lv1_super_dark.png"))
lv1_dark = pg.transform.scale(lv1_dark, size)
lv1_dark_surf = pg.Surface(size, pg.SRCALPHA)
lv1_dark_surf.blit(lv1_dark, (0, 0))

lv1_traps = pg.image.load(os.path.join("levels_image", "level_1", "lv1_lovushka_2.png"))
lv1_traps = pg.transform.scale(lv1_traps, size)
lv1_traps_surf = pg.Surface(size, pg.SRCALPHA)
lv1_traps_surf.blit(lv1_traps, (0, 0))

finish_texture = pg.image.load(os.path.join("levels_image", "final_hole.png"))
finish_texture = pg.transform.scale(finish_texture, [finish_width, finish_hight])
finish_surf = pg.Surface([finish_width, finish_hight], pg.SRCALPHA)
finish_surf.blit(finish_texture, (0, 0))

lv2_walls = pg.image.load(os.path.join("levels_image", "level_2", "lv2_bw.png"))
lv2_walls = pg.transform.scale(lv2_walls, size)
lv2_walls_surf = pg.Surface(size, pg.SRCALPHA)
lv2_walls_surf.blit(lv2_walls, (0, 0))
lv2_traps = pg.image.load(os.path.join("levels_image", "level_2", "lv2_lovyshka.png"))
lv2_traps = pg.transform.scale(lv2_traps, size)
lv2_traps_surf = pg.Surface(size, pg.SRCALPHA)
lv2_traps_surf.blit(lv2_traps, (0, 0))
lv2_dark = pg.image.load(os.path.join("levels_image", "level_2", "lv2_without_guns.png"))
lv2_dark = pg.transform.scale(lv2_dark, size)
lv2_dark_surf = pg.Surface(size, pg.SRCALPHA)
lv2_dark_surf.blit(lv2_dark, (0, 0))

lv3_walls = pg.image.load(os.path.join("levels_image", "level_3", "lv3_light.png"))
lv3_walls = pg.transform.scale(lv3_walls, size)
lv3_walls_surf = pg.Surface(size, pg.SRCALPHA)
lv3_walls_surf.blit(lv3_walls, (0, 0))
lv3_traps = pg.image.load(os.path.join("levels_image", "level_3", "lv3_lovyshki_dark.png"))
lv3_traps = pg.transform.scale(lv3_traps, size)
lv3_traps_surf = pg.Surface(size, pg.SRCALPHA)
lv3_traps_surf.blit(lv3_traps, (0, 0))
lv3_dark = pg.image.load(os.path.join("levels_image", "level_3", "lv3_without_guns.png"))
lv3_dark = pg.transform.scale(lv3_dark, size)
lv3_dark_surf = pg.Surface(size, pg.SRCALPHA)
lv3_dark_surf.blit(lv3_dark, (0, 0))

lv4_walls_g = pg.image.load(os.path.join("levels_image", "level_4", "lv4_without_guns.png"))
lv4_walls_g = pg.transform.scale(lv4_walls_g, size)
lv4_walls_surf_g = pg.Surface(size, pg.SRCALPHA)
lv4_walls_surf_g.blit(lv4_walls_g, (0, 0))
lv4_walls = pg.image.load(os.path.join("levels_image", "level_4", "lv4_light.png"))
lv4_walls = pg.transform.scale(lv4_walls, size)
lv4_walls_surf = pg.Surface(size, pg.SRCALPHA)
lv4_walls_surf.blit(lv4_walls, (0, 0))
lv4_traps = pg.image.load(os.path.join("levels_image", "level_4", "lv4_lovyshki_dark.png"))
lv4_traps = pg.transform.scale(lv4_traps, size)
lv4_traps_surf = pg.Surface(size, pg.SRCALPHA)
lv4_traps_surf.blit(lv4_traps, (0, 0))
lv4_dark = pg.image.load(os.path.join("levels_image", "level_4", "lv4_dark.png"))
lv4_dark = pg.transform.scale(lv4_dark, size)
lv4_dark_surf = pg.Surface(size, pg.SRCALPHA)
lv4_dark_surf.blit(lv4_dark, (0, 0))
