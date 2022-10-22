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
from doctest import TestResults
from sys import exit # Used to exit the game
#------------------------------------------------------------------------------
import pygame
from pygame import mixer
#------------------------------------------------------------------------------
from player import Player
from camera import Camera
from levels import Levels
from music import Music

class NeverEndingCircles:
    def __init__(self):
        # Initialize pygame and set title of the display window
        pygame.init()
        pygame.display.set_caption("Never Ending Circles")

        # Set up fail sound effect
        mixer.init()
        mixer.music.load("assets/sound/fail.mp3")

        # Set up display window to fullscreen
        self.wndSize = (pygame.display.Info().current_w, 
            pygame.display.Info().current_h)
        self.wndCenter = (self.wndSize[0]//2, self.wndSize[1]//2)
        self.screen = pygame.display.set_mode(self.wndSize, pygame.FULLSCREEN)
        
        # Initialize the clock
        self.clock = pygame.time.Clock()
        self.FPS = 60

        # Set up camera
        self.camera = Camera(self.wndSize)
        
        # Set up game state
        self.gameState = "Countdown"

        # Set up levels
        self.levels = Levels(self.wndCenter)

        # Set up tiles sprite group and load the level
        self.tiles = pygame.sprite.Group()
        self.tiles, musicFile, self.BPM = self.levels.loadLevel(self.tiles)
        self.nextTileIndex = 1

        # Set up music
        self.music = Music(musicFile)

        # Set up players and player group
        self.player = pygame.sprite.Group()
        self.player.add(Player("Blue", self.wndSize, self.FPS, self.BPM))
        self.player.add(Player("Orange", self.wndSize, self.FPS, self.BPM))

        # Used to determine whether the moving circle has passed over next tile
        self.passedTile = False

    def mainLoop(self):
        while True:
            # If music not already playing, start playing music
            if self.music.state == "paused":
                self.music.startMusic()

            # Fill background and blit tiles on display window
            self.screen.fill("white")
            self.tiles.draw(self.screen)
            self.tiles.update(self.screen)
            
            # Draw players onto screen and update players' properties
            self.player.draw(self.screen)
            self.player.sprites()[0].update(self.player.sprites()[1])
            self.player.sprites()[1].update(self.player.sprites()[0])
            # Game is running
            if self.gameState == "Running":
                self.running()
            # 3 second countdown before the game starts
            elif self.gameState == "Countdown":
                if pygame.time.get_ticks() >= self.BPM * 30:
                    self.gameState = "Running"
            elif self.gameState == "Idle":
                self.idle()

            pygame.display.update()
            self.clock.tick(self.FPS)


    def running(self):
        # Get blue circle and orange circle sprites
        blueCircle = self.player.sprites()[0]
        orangeCircle = self.player.sprites()[1]
        # Get next tile in path
        nextTile = self.tiles.sprites()[self.nextTileIndex]

        # If the moving circle has collided with the next tile
        if (pygame.sprite.collide_mask(blueCircle, nextTile) and 
        blueCircle.moveState == "Move") or (orangeCircle.moveState == "Move"
        and pygame.sprite.collide_mask(orangeCircle, nextTile)):
            # circle is currently over the tile
            self.passedTile = True
        # If circle has passed over the tile and no longer colliding with tile
        # that means player has failed to hit the input key on time
        elif self.passedTile == True and \
        not pygame.sprite.collide_mask(blueCircle, nextTile) and \
        not pygame.sprite.collide_mask(orangeCircle, nextTile):
            # Play fail sound effect and set the game state to idle
            mixer.music.play()
            self.gameState = "Idle"
            self.music.stopMusic()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # Exit game when escape key pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    self.music.stopMusic()
                    exit()

            if event.type == pygame.KEYDOWN:
                # If circle and tile masks colliding, circle is moving and
                # f key was pressed
                if pygame.sprite.collide_mask(blueCircle, nextTile) and \
                blueCircle.moveState == "Move" and event.key == pygame.K_f:
                    # Snap circle to tile, update the center of circular motion
                    # of other circle and set the other circle to start moving
                    blueCircle.snapToTile(nextTile)
                    # Update camera offset
                    self.camera.centerCam(blueCircle)
                    orangeCircle.moveState = "Move"
                    self.nextTileIndex += 1
                    self.passedTile = False
                    # If next tile has a modifier, update changes to circles
                    if nextTile.modifier != "N":
                        blueCircle.modifierChanges(nextTile)
                        orangeCircle.modifierChanges(nextTile)
                elif pygame.sprite.collide_mask(orangeCircle, nextTile) and \
                orangeCircle.moveState == "Move" and event.key == pygame.K_f:
                    orangeCircle.snapToTile(nextTile)
                    self.camera.centerCam(orangeCircle)
                    blueCircle.moveState = "Move"
                    self.nextTileIndex += 1
                    self.passedTile = False
                    if nextTile.modifier != "N":
                        blueCircle.modifierChanges(nextTile)
                        orangeCircle.modifierChanges(nextTile)

        # Update camera offset and move sprites appropriately
        for sprite in self.player.sprites():
            # If player sprite is not moving and is not centered on the screen
            if sprite.moveState == "Fixed" and \
            sprite.rect.center != self.wndCenter:
                # Center the fixed player
                sprite.rect.center = self.wndCenter
                # Go through each tile and offset their positions
                for tile in self.tiles.sprites():
                    tile.rect.x -= self.camera.offset.x
                    tile.rect.y -= self.camera.offset.y

        # Once final tile is reached, set game state to idle
        if self.nextTileIndex == len(self.tiles.sprites()):
            self.gameState = "Idle"


    def idle(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # Exit game when escape key pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()



if __name__ == "__main__":
    NeverEndingCircles().mainLoop()