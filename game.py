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
from time import sleep # Used for the countdown at the start of the game
#------------------------------------------------------------------------------
import pygame
#------------------------------------------------------------------------------
from player import Player

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
        # Set up players and player group
        self.player = pygame.sprite.Group()
        self.player.add(Player("Blue", self.monitorSize, self.FPS, 1))
        self.player.add(Player("Orange", self.monitorSize, self.FPS, 1))
        # Set up game state
        self.gameState = "Countdown"

    def mainLoop(self):
        while True:
            self.screen.fill("white")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                # Exit game when escape key pressed
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()
                    # Switch movement states of both circles
                    if event.key == pygame.K_d:
                        if (self.player.sprites()[0].moveState == "Move"):
                            self.player.sprites()[0].moveState = "Fixed"
                            self.player.sprites()[1].moveState = "Move"
                        else:
                            self.player.sprites()[0].moveState = "Move"
                            self.player.sprites()[1].moveState = "Fixed"
                    # Rotate direction of circular motion
                    if event.key == pygame.K_r:
                        self.player.sprites()[0].rotationPerSecond = \
                        -(self.player.sprites()[0].rotationPerSecond)
                        self.player.sprites()[1].rotationPerSecond = \
                        -(self.player.sprites()[1].rotationPerSecond)

            # Game is running
            if self.gameState == "Running":
                # Draw players onto screen
                self.player.draw(self.screen)
                self.player.update()
                # Update the center of circular motion of both circles
                self.player.sprites()[0].updateCircMotionCenter(
                    self.player.sprites()[1])
                self.player.sprites()[1].updateCircMotionCenter(
                    self.player.sprites()[0])
            # Countdown before the game starts
            elif self.gameState == "Countdown":
                self.player.draw(self.screen)
                pygame.display.update()
                sleep(3)
                self.gameState = "Running"

            pygame.display.update()
            self.clock.tick(self.FPS)

NeverEndingCircles().mainLoop()