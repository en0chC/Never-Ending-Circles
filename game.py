#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# Author : Enoch Luis S Catuncan
# Date Created : October 15th 2022
# version = '1.0'
#------------------------------------------------------------------------------
"""
This module contains the main logic of the game and is what will be imported 
by the __main__ file.
"""
#------------------------------------------------------------------------------
from sys import exit # Used to exit the game
#------------------------------------------------------------------------------
import pygame

class NeverEndingCircles:
    def __init__(self):
        # Initialize pygame and set title of the display window
        pygame.init()
        pygame.display.set_caption("Never Ending Circles")
        # Set up display window
        self.monitorSize = (
            pygame.display.Info().current_w, 
            pygame.display.Info().current_h
            )
        self.screen = pygame.display.set_mode(
            self.monitorSize, 
            pygame.FULLSCREEN
            )
        # Initialize the clock
        self.clock = pygame.time.Clock()
        self.FPS = 60

    def mainLoop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            pygame.display.update()

            self.clock.tick(self.FPS)

NeverEndingCircles().mainLoop()