#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# Author : Enoch Luis S Catuncan
# Date Created : October 15th 2022
#------------------------------------------------------------------------------
"""
This module contains the main logic and main loop of the game and is what will 
be imported by the __main__ file.
"""
#------------------------------------------------------------------------------
from tkinter import Tk
#------------------------------------------------------------------------------
import pygame
#------------------------------------------------------------------------------
from gameStates import Title
from server import Server, loginWindow
#------------------------------------------------------------------------------

class NeverEndingCircles:
    def __init__(self):
        # Initialize pygame and set title of the display window
        pygame.init()
        pygame.display.set_caption("Never Ending Circles")

        # Initialize server capabilities and display the login window
        self.server = Server()
        self.username = None
        self.loggedin = False
        loginWindow(Tk(), self.server, self)
        # Continue if logged in successfully
        if not self.loggedin:
            quit()

        # Set up display window to fullscreen and load main menu image
        self.wndSize = (pygame.display.Info().current_w, 
            pygame.display.Info().current_h)
        self.wndCenter = (self.wndSize[0]//2, self.wndSize[1]//2)
        self.screen = pygame.display.set_mode(self.wndSize, pygame.FULLSCREEN)
        self.menuImage = pygame.image.load(
            "assets/images/backgrounds/mainmenu.jpg")
        
        # Initialize the variables dealing with time
        self.clock = pygame.time.Clock()
        self.FPS = 60
        # Counter for the countdown when starting the level
        self.countdownCounter = 3
        # Counter for resetting the pressed status of hit key
        self.counterTimer = None

        # Initialize variables used in Gameplay state (while running a level)
        # Initialized as None or empty as values depend on the level being run
        self.camera = None
        self.music = None
        self.BPM = None
        self.levels = None
        self.background = None
        self.checkpoints = [0]
        self.checkpointScore = [0]
        self.checkpointMusicTime = [0.0]

        # Initialize sprite groups for the players and tiles
        self.player = pygame.sprite.Group()
        self.tiles = pygame.sprite.Group()

        # Variable used to turn "Invincible" mode on or off
        self.invincible = False
        # Keeps track of whether invincible mode was used
        self.turnedOnInvincible = False
        
        # Set up text fonts
        self.titleFont = pygame.font.Font("assets/fonts/GodoMaum.ttf", 140)
        self.mainFont = pygame.font.Font("assets/fonts/UnmaskedBb.ttf", 50)
        self.scoreFont = pygame.font.Font("assets/fonts/UnmaskedBb.ttf", 15)

        # Tracks key presses of the player
        self.keysPressed = {
            "hit": False,
            "enter": False,
            "escape": False,
            "up": False,
            "down": False,
            "r": False
            }

        # Set up and run initial game state
        self.stateStack = []
        self.titleScreen = Title(self)
        self.stateStack.append(self.titleScreen)

    # Main loop that runs the game
    def mainLoop(self):
        while True:
            # Game is run by first getting user key presses, updating sprites
            # and game states and rendering any text and sprite onto screen
            # The game state at the top of the stack is the one being run
            self.getKeyPresses()
            self.stateStack[-1].update(self.keysPressed)
            self.stateStack[-1].render(self.screen)
            pygame.display.update()
            self.clock.tick(self.FPS)

    # Gets key presses from user and updates keysPressed dictionary accordingly
    def getKeyPresses(self):
        for event in pygame.event.get():
            # When a key is pressed down, update its status to True in the dict
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
                    # Start the timer for resetting the hit key
                    pygame.time.set_timer(pygame.USEREVENT + 1, 200)
                if event.key == pygame.K_r:
                    self.keysPressed["r"] = True
                if event.key == pygame.K_RETURN:
                    self.keysPressed["enter"] = True
            # When a key is unpressed, update its status to False in the dict
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    self.keysPressed["escape"] = False
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    self.keysPressed["up"] = False
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    self.keysPressed["down"] = False
                if event.key == pygame.K_r:
                    self.keysPressed["r"] = False
                if event.key == pygame.K_RETURN:
                    self.keysPressed["enter"] = False
            # Decrement countdown timer after specified amount of time
            if event.type == pygame.USEREVENT:
                self.countdownCounter -= 1
            # Set pressed state of hit key to false after timer tick
            if event.type == pygame.USEREVENT + 1:
                self.keysPressed["hit"] = False
                pygame.time.set_timer(pygame.USEREVENT + 1, 0)

    # Template used to draw text onto the screen
    def drawText(self, display, font, text, color, x, y):
        if font == "Title":
            textImage = self.titleFont.render(text, True, color)
        if font == "Main":
            textImage = self.mainFont.render(text, True, color)
        if font == "Score":
            textImage = self.scoreFont.render(text, True, color)
        textRect = textImage.get_rect(center=(x, y))
        display.blit(textImage, textRect)

    # Reset status of keys to unpressed
    # Allows key inputs to be recognized only after initial press
    def resetKeysPressed(self):
        for key in self.keysPressed:
            # Hit key has its own timer so don't reset it
            if key != "hit":
                self.keysPressed[key] = False

    # Resets variables related to the running of a level
    # Used when restarting and loading levels
    def resetLevelState(self):
        self.camera = None
        self.music = None
        self.BPM = None
        self.levels = None
        self.background = None
        self.countdownCounter = 3
        pygame.time.set_timer(pygame.USEREVENT, 0)
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.Group()

    # Resets variables related to keeping track of checkpoints
    # Seperate from resetLevelState, prevents checkpoint reset after restarting
    def resetCheckpointState(self):
        self.checkpoints = [0]
        self.checkpointScore = [0]
        self.checkpointMusicTime = [0.0]