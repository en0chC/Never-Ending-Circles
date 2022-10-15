#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# Author : Enoch Luis S Catuncan
# Date Created : October 15th 2022
# version = '1.0'
#------------------------------------------------------------------------------
"""
This module contains the player sprite.
"""
#------------------------------------------------------------------------------
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, type, movementState, windowSize):
        super().__init__()
        self.type = type
        # Circle is either fixed in place or moving in a circle
        self.moveState = movementState
        # Set up blue or orange circle image and rect
        if type == "Blue":
            self.image = pygame.image.load("assets/images/blue_circle.png")
            self.image = pygame.transform.scale(self.image, (50, 50))
            self.rect = self.image.get_rect(
                center=(windowSize[0] // 2, windowSize[1] // 2))
        else:
            self.image = pygame.image.load("assets/images/orange_circle.png")
            self.image = pygame.transform.scale(self.image, (50, 50))
            self.rect = self.image.get_rect(
                center=(windowSize[0] // 2 + 100, windowSize[1] // 2))
        
    def move(self):
        if self.moveState == "Move":
            self.rect.x += 1
            self.rect.y += 1

    def update(self):
        self.move()