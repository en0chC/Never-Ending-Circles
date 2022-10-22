#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# Author : Enoch Luis S Catuncan
# Date Created : October 15th 2022
# version = '1.0'
#------------------------------------------------------------------------------
"""
This module contains the Tile sprite.
"""
#------------------------------------------------------------------------------
import pygame

class Tile(pygame.sprite.Sprite):
    # pos is TEMPORARY
    def __init__(self, wndCenter, pos, tileType):
        super().__init__()
        # Set up tile image and rect
        self.image = pygame.image.load(
            "assets/images/" + tileType + ".png").convert_alpha()

        self.rect = self.image.get_rect(
            center=(wndCenter[0] + pos[0], wndCenter[1] + pos[1]))
        self.offset = pygame.math.Vector2()
        # Set up mask for collision detection
        self.mask = pygame.mask.from_surface(self.image)