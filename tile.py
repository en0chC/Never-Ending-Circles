#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# Author : Enoch Luis S Catuncan
# Date Created : October 15th 2022
#------------------------------------------------------------------------------
"""
This module contains the Tile sprite class which initializes tile sprites.
"""
#------------------------------------------------------------------------------
import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, wndCenter, pos, tileType, modifier, currentBPM):
        super().__init__()
        # Set up tile image, rect and modifier
        self.image = pygame.image.load(
            "assets/images/" + tileType + ".png").convert_alpha()
        self.rect = self.image.get_rect(
            center=(wndCenter[0] + pos[0], wndCenter[1] + pos[1]))
        self.modifier = modifier

        # If modifier is change in speed
        if modifier[0] == "S":
            self.modifier = "S"
            # BPM to switch to
            self.modifierBPM = float(modifier[3:9])
            # If new BPM is higher than current BPM, use speed up image
            if self.modifierBPM > currentBPM:
                self.modifierImage = pygame.image.load(
                    "assets/images/speedup.png").convert_alpha()
            else:
                self.modifierImage = pygame.image.load(
                    "assets/images/slowdown.png").convert_alpha()
        # If modifier is reverse direction
        if modifier[0] == "R":
            self.modifier = "R"
            self.modifierImage = pygame.image.load(
                "assets/images/reverse.png").convert_alpha()
        # If modifier is checkpoint
        if modifier[0] == "C":
            self.modifier = "C"
            self.modifierImage = pygame.image.load(
                "assets/images/checkpoint.png").convert_alpha()
        # Set up mask for collision detection
        self.mask = pygame.mask.from_surface(self.image)

    # Update the modifier image of the tile
    def updateModifierImage(self, screen):
        # If tile modifier is not 'Normal', blit modifier image
        if self.modifier != "N":
            screen.blit(self.modifierImage, self.rect)

    def update(self, screen):
        self.updateModifierImage(screen)