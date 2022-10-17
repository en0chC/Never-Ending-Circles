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
        self.wndSize = windowSize
        self.offset = pygame.math.Vector2(0, 0)

    def follow(self, player):
        if player.moveState == "Move":
            self.offset.x += player.rect.x - self.offset.x
            self.offset.y += player.rect.y - self.offset.y