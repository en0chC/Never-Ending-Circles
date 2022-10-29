#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# Author : Enoch Luis S Catuncan
# Date Created : October 29th 2022
# version = '1.0'
#------------------------------------------------------------------------------
"""

"""
#------------------------------------------------------------------------------
from sys import exit # Used to exit the game
#------------------------------------------------------------------------------
import pygame
from pygame import mixer
#------------------------------------------------------------------------------
from levels import Levels
from music import Music
from player import Player
from camera import Camera

class GameState:
    def __init__(self, game):
        self.game = game
        self.prevState = -1

    def nextState(self):
        self.prevState += 1
        self.game.stateStack.append(self)

    def exitState(self):
        self.prevState -= 1
        self.game.stateStack.pop()

class Title(GameState):
    def __init__(self, game):
        super().__init__(game)

    def update(self, keysPressed):
        if keysPressed["enter"]:
            newState = MainMenu(self.game)
            newState.nextState()
        self.game.resetKeysPressed()
    
    def render(self, screen):
        screen.fill((0, 0, 0))
        self.game.drawText(screen, "Title", "Never Ending Circles", 
        (255, 255, 255), self.game.wndCenter[0], self.game.wndCenter[1])

class MainMenu(GameState):
    def __init__(self, game):
        super().__init__(game)
        self.game = game
        self.menuOptions = ["Start", "Exit"]
        self.menuIndex = 0
        self.startColor = (211, 81, 84)
        self.exitColor = (255, 255, 255)
    
    def update(self, keysPressed):
        self.updateSelected(keysPressed)
        if keysPressed["enter"]:
            if self.menuOptions[self.menuIndex] == "Start":
                newState = LevelTransition(self.game, 0)
                newState.nextState()
            if self.menuOptions[self.menuIndex] == "Exit":
                pygame.quit()
                exit()
        self.game.resetKeysPressed()

    def render(self, screen):
        screen.fill((0, 0, 0))
        self.game.drawText(screen, "Title", "Never Ending Circles", 
        (255, 255, 255), self.game.wndCenter[0], self.game.wndSize[1]*0.2)
        self.game.drawText(screen, "Main", "Start",
        self.startColor, self.game.wndCenter[0], self.game.wndSize[1]*0.5)
        self.game.drawText(screen, "Main", "Exit",
        self.exitColor, self.game.wndCenter[0], self.game.wndSize[1]*0.6)

    def updateSelected(self, keysPressed):
        if keysPressed["up"]:
            self.menuIndex = (self.menuIndex - 1) % len(self.menuOptions)
        elif keysPressed["down"]:
            self.menuIndex = (self.menuIndex + 1) % len(self.menuOptions)
        
        self.startColor = (255, 255, 255)
        self.exitColor = (255, 255, 255)
        if self.menuIndex == 0:
            self.startColor = (211, 81, 84)
        if self.menuIndex == 1:
            self.exitColor = (211, 81, 84)

class LevelTransition(GameState):
    def __init__(self, game, level):
        super().__init__(game)
        self.game = game

        self.game.screen.fill((0, 0, 0))
        self.game.drawText(self.game.screen, "Main", "Loading...", 
        (255, 255, 255), self.game.wndCenter[0], self.game.wndCenter[1])

        self.levels = Levels(self.game.wndCenter)
        self.game.tiles.empty()
        self.game.tiles, self.game.music, self.game.BPM = \
            self.levels.loadLevel(self.game.tiles, level)
        self.game.music = Music(self.game.music)

        self.game.player.empty()
        self.game.player.add(Player("Blue", self.game.wndSize, 
            self.game.FPS, self.game.BPM))
        self.game.player.add(Player("Orange", self.game.wndSize, 
            self.game.FPS, self.game.BPM))

    def update(self, keysPressed):
        if keysPressed["enter"]:
            newState = Gameplay(self.game)
            newState.nextState()
        if keysPressed["escape"]:
            newState = PauseMenu(self.game)
            newState.nextState()

    def render(self, screen):
        screen.fill((0, 0, 0))
        self.game.tiles.draw(screen)
        self.game.player.draw(screen)

class Gameplay(GameState):
    def __init__(self, game):
        super().__init__(game)
        self.game = game
        self.game.camera = Camera(self.game.wndSize)
        self.gameState = "NotStarted"
        self.nextTileIndex = 1
        self.passedTile = False
        
        self.countdownStartTick = 0
        self.countdownTimer = 3

        mixer.init()
        mixer.music.load("assets/sound/fail.mp3")

    def update(self, keysPressed):
        if keysPressed["enter"] and self.gameState == "NotStarted":
            self.game.music.startMusic()
            self.countdownStartTick = pygame.time.get_ticks()
            self.gameState = "Countdown"
        if keysPressed["escape"]:
            self.game.music.pause()
            newState = PauseMenu(self.game)
            newState.nextState()

        if self.gameState != "NotStarted":
            self.game.tiles.update(self.game.screen)
            self.game.player.sprites()[0].update(self.game.player.sprites()[1])
            self.game.player.sprites()[1].update(self.game.player.sprites()[0])

        if keysPressed["r"]:
            self.game.music.stopMusic()
            self.game.stateStack.pop()
            self.game.stateStack.pop()
            newState = LevelTransition(self.game, 0)
            newState.nextState()

        if self.gameState == "Countdown":
            self.countdown()
        if self.gameState == "Gameplay":
            self.gameplay(keysPressed)
        if self.gameState == "Failed":
            self.failed(keysPressed)
        if self.gameState == "Won":
            self.won(keysPressed)

        self.game.resetKeysPressed()

    def render(self, screen):
        screen.fill((0, 0, 0))
        self.game.tiles.draw(screen)
        self.game.player.draw(screen)
        if self.gameState == "Countdown":
            self.game.drawText(screen, "Main", str(self.countdownTimer),
            (255, 255, 255), self.game.wndCenter[0], self.game.wndSize[1]*0.25)
        if self.gameState == "Failed":
            self.game.drawText(screen, "Main", "Press enter to restart",
            (255, 255, 255), self.game.wndCenter[0], self.game.wndSize[1]*0.25)
        if self.gameState == "Won":
            self.game.drawText(screen, "Main", 
            "You Won!\nPress enter to return to the main menu",
            (255, 255, 255), self.game.wndCenter[0], self.game.wndSize[1]*0.25)

    def countdown(self):
        self.countdownTimer = \
        3 - (pygame.time.get_ticks() - self.countdownStartTick)//1000
        if self.countdownTimer == 0:
            self.gameState = "Gameplay"

    def gameplay(self, keysPressed):
        # Get blue circle and orange circle sprites
        blueCircle = self.game.player.sprites()[0]
        orangeCircle = self.game.player.sprites()[1]
        # Get next tile in path
        nextTile = self.game.tiles.sprites()[self.nextTileIndex]

        # If the moving circle has collided with the next tile
        if (pygame.sprite.collide_mask(blueCircle, nextTile) and 
        blueCircle.moveState == "Move") or \
        (pygame.sprite.collide_mask(orangeCircle, nextTile) and
        orangeCircle.moveState == "Move"):
            # circle is currently over the tile
            self.passedTile = True
        # If circle has passed over the tile and no longer colliding with tile
        # that means player has failed to hit the input key on time
        elif self.passedTile == True and \
        not pygame.sprite.collide_mask(blueCircle, nextTile) and \
        not pygame.sprite.collide_mask(orangeCircle, nextTile):
            # Play fail sound effect and set the game state to failed
            mixer.music.play()
            self.gameState = "failed"
            self.game.music.stopMusic()

        # If circle and tile masks colliding, circle is moving and
        # one of the hit keys were pressed
        if pygame.sprite.collide_mask(blueCircle, nextTile) and \
        blueCircle.moveState == "Move" and keysPressed["hit"]:
            # Snap circle to tile, update the center of circular motion
            # of other circle and set the other circle to start moving
            blueCircle.snapToTile(nextTile)
            # Update camera offset
            self.game.camera.centerCam(blueCircle)
            orangeCircle.moveState = "Move"
            self.nextTileIndex += 1
            self.passedTile = False
            # If next tile has a modifier, update changes to circles
            if nextTile.modifier != "N":
                blueCircle.modifierChanges(nextTile)
                orangeCircle.modifierChanges(nextTile)
        elif pygame.sprite.collide_mask(orangeCircle, nextTile) and \
        orangeCircle.moveState == "Move" and keysPressed["hit"]:
            orangeCircle.snapToTile(nextTile)
            self.game.camera.centerCam(orangeCircle)
            blueCircle.moveState = "Move"
            self.nextTileIndex += 1
            self.passedTile = False
            if nextTile.modifier != "N":
                blueCircle.modifierChanges(nextTile)
                orangeCircle.modifierChanges(nextTile)

        # Update camera offset and move sprites appropriately
        for sprite in self.game.player.sprites():
            # If player sprite is not moving and is not centered on the screen
            if sprite.moveState == "Fixed" and \
            sprite.rect.center != self.game.wndCenter:
                # Center the fixed player
                sprite.rect.center = self.game.wndCenter
                # Go through each tile and offset their positions
                for tile in self.game.tiles.sprites():
                    tile.rect.x -= self.game.camera.offset.x
                    tile.rect.y -= self.game.camera.offset.y

        # Once final tile is reached, set game state to failed
        if self.nextTileIndex == len(self.game.tiles.sprites()):
            self.gameState = "failed"

    def failed(self, keysPressed):
        self.game.music.stopMusic()
        if keysPressed["enter"]:
            self.game.stateStack.pop()

    def won(self, keysPressed):
        if keysPressed["enter"]:
            while len(self.game.stateStack) != 2:
                self.game.stateStack.pop()

class PauseMenu(GameState):
    def __init__(self, game):
        super().__init__(game)
        self.game = game
        self.menuOptions = ["Resume", "ExitToMainMenu"]
        self.menuIndex = 0
        self.resumeColor = (211, 81, 84)
        self.exitColor = (255, 255, 255)
    
    def update(self, keysPressed):
        self.updateSelected(keysPressed)
        if keysPressed["enter"]:
            if self.menuOptions[self.menuIndex] == "Resume":
                self.game.music.unpause()
                self.game.stateStack.pop()
            if self.menuOptions[self.menuIndex] == "ExitToMainMenu":
                while len(self.game.stateStack) != 2:
                    self.game.stateStack.pop()
        self.game.resetKeysPressed()

    def render(self, screen):
        self.game.drawText(screen, "Main", "Resume",
        self.resumeColor, self.game.wndCenter[0], self.game.wndSize[1]*0.4)
        self.game.drawText(screen, "Main", "Exit to Main Menu",
        self.exitColor, self.game.wndCenter[0], self.game.wndSize[1]*0.6)

    def updateSelected(self, keysPressed):
        if keysPressed["up"]:
            self.menuIndex = (self.menuIndex - 1) % len(self.menuOptions)
        elif keysPressed["down"]:
            self.menuIndex = (self.menuIndex + 1) % len(self.menuOptions)
        
        self.resumeColor = (255, 255, 255)
        self.exitColor = (255, 255, 255)
        if self.menuIndex == 0:
            self.resumeColor = (211, 81, 84)
        if self.menuIndex == 1:
            self.exitColor = (211, 81, 84)