#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# Author : Enoch Luis S Catuncan
# Date Created : October 15th 2022
#------------------------------------------------------------------------------
"""
This module contains the Camera class which is used to calculate offset in
player movement. The offset is used to modify player and tile coordinates to 
keep the camera centered on the player.
"""
#------------------------------------------------------------------------------
import pygame

class Camera:
    def __init__(self, windowSize):
        self.wndCenter = (windowSize[0]//2, windowSize[1]//2)
        self.offset = pygame.math.Vector2()
        self.offsetdx = 0
        self.offsetdy = 0

    def centerCam(self, player):
        self.offset.x = player.rect.center[0] - self.wndCenter[0]
        self.offset.y = player.rect.center[1] - self.wndCenter[1]

    # Calculates offset from player's position to center of the screen
    def updateOffset(self, player):
        if player.rect.center[0] > self.wndCenter[0]:
            self.offsetdx = -5
        elif player.rect.center[0] < self.wndCenter[0]:
            self.offsetdx = 5
        else:
            self.offsetdx = 0

        if player.rect.center[1] > self.wndCenter[1]:
            self.offsetdy = -5
        elif player.rect.center[1] < self.wndCenter[1]:
            self.offsetdy = 5
        else:
            self.offsetdy = 0