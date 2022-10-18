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
#------------------------------------------------------------------------------
from player import Player
from tile import Tile
from camera import Camera

class NeverEndingCircles:
    def __init__(self):
        # Initialize pygame and set title of the display window
        pygame.init()
        pygame.display.set_caption("Never Ending Circles")
        # Set up display window to fullscreen
        self.wndSize = (
            pygame.display.Info().current_w, pygame.display.Info().current_h)
        self.wndCenter = (self.wndSize[0]//2, self.wndSize[1]//2)
        self.screen = pygame.display.set_mode(
            self.wndSize, pygame.FULLSCREEN)
        # Initialize the clock
        self.clock = pygame.time.Clock()
        self.FPS = 60
        # Set up players and player group
        self.player = pygame.sprite.Group()
        self.player.add(Player("Blue", self.wndSize, self.FPS, 1))
        self.player.add(Player("Orange", self.wndSize, self.FPS, 1))
        # Set up camera
        self.camera = Camera(self.wndSize)
        # Set up game state
        self.gameState = "Countdown"

        # Set up test tiles and tiles group (TEMPORARY)
        self.tiles = pygame.sprite.Group()
        self.tiles.add(Tile(self.wndSize, (0, 0)))
        self.tiles.add(Tile(self.wndSize, (100, 0)))
        self.tiles.add(Tile(self.wndSize, (200, 0)))
        self.tiles.add(Tile(self.wndSize, (300, 0)))
        self.tiles.add(Tile(self.wndSize, (400, 0)))
        self.tiles.add(Tile(self.wndSize, (500, 0)))
        self.tiles.add(Tile(self.wndSize, (600, 0)))
        self.tiles.add(Tile(self.wndSize, (700, 0)))
        self.tiles.add(Tile(self.wndSize, (800, 0)))
        self.tiles.add(Tile(self.wndSize, (900, 0)))
        self.nextTileIndex = 1

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
                        exit()
            
            self.camera.centerCam(self.player.sprites()[0])
            self.camera.centerCam(self.player.sprites()[1])

            # Fill background and blit tiles on display window
            self.screen.fill("white")
            for sprite in self.tiles.sprites():
                if self.player.sprites()[0].rect.center != self.wndCenter and \
                self.player.sprites()[1].rect.center != self.wndCenter:
                    sprite.rect.x -= self.camera.offset.x
                    sprite.rect.y -= self.camera.offset.y
            self.tiles.draw(self.screen)

            for sprite in self.player.sprites():
                if sprite.moveState == "Fixed" and \
                sprite.rect.center != self.wndCenter:
                    sprite.rect.x -= self.camera.offset.x
                    sprite.rect.y -= self.camera.offset.y

            """
            for sprite in self.player.sprites():
                if sprite.moveState == "Fixed" and \
                sprite.rect.centerx - self.wndSize[0]//2 <= 5 and \
                sprite.rect.centery - self.wndSize[1]//2 <= 5:
                    sprite.rect.center = self.wndCenter
                elif sprite.moveState == "Fixed" and \
                sprite.rect.center != self.wndCenter:
                    sprite.rect.x -= self.camera.offset.x
                    sprite.rect.y -= self.camera.offset.y
            """

            # Draw players onto screen and update players' properties
            self.player.draw(self.screen)
            self.player.sprites()[0].update(self.player.sprites()[1])
            self.player.sprites()[1].update(self.player.sprites()[0])
            # Game is running
            if self.gameState == "Running":
                self.running()
            # 3 second countdown before the game starts
            elif self.gameState == "Countdown":
                if pygame.time.get_ticks() >= 3000:
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
            orangeCircle.snapToTile(nextTile)
            # Update camera offset
            self.camera.centerCam(orangeCircle)
            blueCircle.update(orangeCircle)
            blueCircle.moveState = "Move"
            self.nextTileIndex += 1

        # Once final tile is reached, set game state to idle
        if self.nextTileIndex == len(self.tiles.sprites()):
            self.gameState = "Idle"

if __name__ == "__main__":
    NeverEndingCircles().mainLoop()