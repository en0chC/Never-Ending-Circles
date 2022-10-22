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

        # Set up tile snap sound effect
        mixer.init()
        mixer.music.load("assets/sound/hit.mp3")
        mixer.music.set_volume(0.2)

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
        self.tiles, musicFile, BPM = self.levels.loadLevel(self.tiles)
        self.nextTileIndex = 1

        # Set up music
        self.music = Music(musicFile)

        # Set up players and player group
        self.player = pygame.sprite.Group()
        self.player.add(Player("Blue", self.wndSize, self.FPS, BPM))
        self.player.add(Player("Orange", self.wndSize, self.FPS, BPM))

    def mainLoop(self):
        while True:
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

            # If music not already playing, start playing music
            if self.music.state == "paused":
                self.music.startMusic()

            # Fill background and blit tiles on display window
            self.screen.fill("white")
            self.tiles.draw(self.screen)
            
            # Draw players onto screen and update players' properties
            self.player.draw(self.screen)
            self.player.sprites()[0].update(self.player.sprites()[1])
            self.player.sprites()[1].update(self.player.sprites()[0])
            # Game is running
            if self.gameState == "Running":
                self.running()
            # 3 second countdown before the game starts
            elif self.gameState == "Countdown":
                if pygame.time.get_ticks() >= 4000:
                    self.gameState = "Running"
            elif self.gameState == "Idle":
                pass

            pygame.display.update()
            self.clock.tick(self.FPS)


    def running(self):
        # Get blue circle and orange circle sprites
        blueCircle = self.player.sprites()[0]
        orangeCircle = self.player.sprites()[1]

        # Get keys being pressed
        keys = pygame.key.get_pressed()
        nextTile = self.tiles.sprites()[self.nextTileIndex]

        # If circle and tile masks colliding, circle is moving and
        # f key being pressed
        if pygame.sprite.collide_mask(blueCircle, nextTile) and \
        blueCircle.moveState == "Move" and keys[pygame.K_f]:
            # Play tile snap sound effect
            mixer.music.play()
            # Snap circle to tile, update the center of circular motion of 
            # other circle and set the other circle to start moving
            blueCircle.snapToTile(nextTile)
            # Update camera offset
            self.camera.centerCam(blueCircle)
            orangeCircle.update(blueCircle)
            orangeCircle.moveState = "Move"
            self.nextTileIndex += 1
        elif pygame.sprite.collide_mask(orangeCircle, nextTile) and \
        orangeCircle.moveState == "Move" and keys[pygame.K_f]:
            mixer.music.play()
            orangeCircle.snapToTile(nextTile)
            self.camera.centerCam(orangeCircle)
            blueCircle.update(orangeCircle)
            blueCircle.moveState = "Move"
            self.nextTileIndex += 1

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



if __name__ == "__main__":
    NeverEndingCircles().mainLoop()