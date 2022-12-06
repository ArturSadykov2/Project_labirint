import pygame as pg


def create_masks(surf):
    pg.mask.from_surface(surf)
    return surf
