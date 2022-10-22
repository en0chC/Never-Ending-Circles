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
        self.offset = pygame.math.Vector2()
        self.deltax = 0
        self.deltay = 0

    def centerCam(self, player):
        self.offset.x = player.rect.center[0] - self.wndCenter[0]
        self.offset.y = player.rect.center[1] - self.wndCenter[1]