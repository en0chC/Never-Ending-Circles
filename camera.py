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
    def __init__(self, player, windowSize):
        vec = pygame.math.Vector2
        self.player = player
        self.offset = vec(0, 0)
        self.offsetFloat = vec(0, 0)
        self.windowSize = windowSize