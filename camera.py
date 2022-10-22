#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# Author : Enoch Luis S Catuncan
# Date Created : October 15th 2022
# version = '1.0'
#------------------------------------------------------------------------------
"""
This module contains the Camera class.
"""
#------------------------------------------------------------------------------
import pygame

class Camera:
    def __init__(self, windowSize):
        self.wndCenter = (windowSize[0]//2, windowSize[1]//2)
        self.offset = pygame.math.Vector2(0, 0)
        self.deltax = 0
        self.deltay = 0

    def centerCam(self, player):
        # If fixed circle is 100 pixels away from center, means it has just
        # snapped to the tile, so update change in x and y coordinates
        if player.moveState == "Fixed" and \
        ((player.rect.center[0] - self.wndCenter[0])**2 
        + (player.rect.center[1] - self.wndCenter[1])**2)**(1/2) == 100:
            print(player.angle)
            self.deltax = player.rect.center[0] - self.wndCenter[0] / 10
            self.deltay = player.rect.center[1] - self.wndCenter[1] / 10
            self.offset.x = self.deltax / 10
            self.offset.y = self.deltay / 10