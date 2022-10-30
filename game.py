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
import pygame
#------------------------------------------------------------------------------
from gameStates import Title

class NeverEndingCircles:
    def __init__(self):
        # Initialize pygame and set title of the display window
        pygame.init()
        pygame.display.set_caption("Never Ending Circles")

        # Set up display window to fullscreen
        self.wndSize = (
            pygame.display.Info().current_w, 
            pygame.display.Info().current_h)
        self.wndCenter = (self.wndSize[0]//2, self.wndSize[1]//2)
        self.screen = pygame.display.set_mode(self.wndSize, pygame.FULLSCREEN)
        
        # Initialize the clock
        self.clock = pygame.time.Clock()
        self.FPS = 60

        self.camera = None
        self.music = None
        self.BPM = None
        self.checkpoints = [0]
        self.checkpointScore = [0]
        self.checkpointMusicTime = [0.0]
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.Group()
        
        # Set up text fonts
        self.titleFont = pygame.font.Font("assets/fonts/GodoMaum.ttf", 140)
        self.mainFont = pygame.font.Font("assets/fonts/UnmaskedBb.ttf", 50)
        self.scoreFont = pygame.font.Font("assets/fonts/UnmaskedBb.ttf", 15)

        # Track key presses of the player
        self.keysPressed = {
            "hit": False,
            "enter": False,
            "escape": False,
            "up": False,
            "down": False,
            "r": False
            }

        # Set up game state
        self.stateStack = []
        self.loadState()

    def mainLoop(self):
        while True:
            self.getKeyPresses()
            self.stateStack[-1].update(self.keysPressed)
            self.stateStack[-1].render(self.screen)
            pygame.display.update()
            self.clock.tick(self.FPS)

    def getKeyPresses(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.keysPressed["escape"] = True
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    self.keysPressed["up"] = True
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    self.keysPressed["down"] = True
                if event.key == pygame.K_f or event.key == pygame.K_j or \
                event.key == pygame.K_d or event.key == pygame.K_k:
                    self.keysPressed["hit"] = True
                if event.key == pygame.K_r:
                    self.keysPressed["r"] = True
                if event.key == pygame.K_RETURN:
                    self.keysPressed["enter"] = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    self.keysPressed["escape"] = False
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    self.keysPressed["up"] = False
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    self.keysPressed["down"] = False
                if event.key == pygame.K_f or event.key == pygame.K_j or \
                event.key == pygame.K_d or event.key == pygame.K_k:
                    self.keysPressed["hit"] = False
                if event.key == pygame.K_r:
                    self.keysPressed["r"] = False
                if event.key == pygame.K_RETURN:
                    self.keysPressed["enter"] = False

    def drawText(self, display, font, text, color, x, y):
        if font == "Title":
            textImage = self.titleFont.render(text, True, color)
        if font == "Main":
            textImage = self.mainFont.render(text, True, color)
        if font == "Score":
            textImage = self.scoreFont.render(text, True, color)
        textRect = textImage.get_rect(center=(x, y))
        display.blit(textImage, textRect)

    def resetKeysPressed(self):
        for key in self.keysPressed:
            self.keysPressed[key] = False

    def loadState(self):
        self.titleScreen = Title(self)
        self.stateStack.append(self.titleScreen)

if __name__ == "__main__":
    NeverEndingCircles().mainLoop()