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
    def __init__(self, windowSize, pos):
        super().__init__()
        # Set up tile image and rect
        self.image = pygame.image.load(
            "assets/images/StoN.png").convert_alpha()
            
        # TEMPORARY
        self.image = pygame.transform.rotate(self.image, 90)

        self.rect = self.image.get_rect(
            center=(windowSize[0]//2 + pos[0], windowSize[1]//2 + pos[1]))
        self.offset = pygame.math.Vector2()
        # Set up mask for collision detection
        self.mask = pygame.mask.from_surface(self.image)