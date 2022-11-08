#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# Author : Enoch Luis S Catuncan
# Date Created : October 29th 2022
#------------------------------------------------------------------------------
"""
This module contains the different game state classes that the game can be in. 
State classes are popped and pushed onto a stack located in the main game class, 
allowing a hierarchical structure of game states and transitioning into and back
to different game states. These game states all have two functions in common,
'update' and 'render' which allows the main game class to call these methods on
whichever state class is at the top of the stack. 
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
from background import Background
from particle import Particle
#------------------------------------------------------------------------------

# Parent class that game state child classes inherit from
class GameState:
    def __init__(self, game):
        self.game = game

    # Push game state onto the state stack
    def nextState(self):
        self.game.stateStack.append(self)
    
    # Pop game state from the state stack
    def exitState(self):
        self.game.stateStack.pop()

# Title screen game state that is accessed first when opening the game
class Title(GameState):
    def __init__(self, game):
        super().__init__(game)

    # Checks for any key presses and updates the game appropriately
    def update(self, keysPressed):
        if keysPressed["enter"]:
            # Create new game state class and push it onto the stack
            newState = MainMenu(self.game)
            newState.nextState()
        # Reset status of key presses
        self.game.resetKeysPressed()
    
    # Draws any text and sprite specific to the game state onto the screen
    def render(self, screen):
        screen.fill((0, 0, 0))
        screen.blit(self.game.menuImage, (0, 0))
        self.game.drawText(screen, "Title", "Never Ending Circles", 
        (255, 255, 255), self.game.wndCenter[0], self.game.wndCenter[1])

# Main menu with options to start level select, view leaderboards or exit game
class MainMenu(GameState):
    def __init__(self, game):
        super().__init__(game)
        self.game = game
        # Keeps track of the menu option being currently selected
        self.menuOptions = ["Start", "Leaderboards", "Exit"]
        self.menuIndex = 0
        # Color of the text to show user which one is currently highlighted
        self.startColor = (211, 81, 84)
        self.leaderboardsColor = (255, 255, 255)
        self.exitColor = (255, 255, 255)
    
    def update(self, keysPressed):
        self.updateSelected(keysPressed)
        # When enter is pressed, select option that is currently highlighted
        if keysPressed["enter"]:
            if self.menuOptions[self.menuIndex] == "Start":
                newState = LevelSelect(self.game)
                newState.nextState()
            if self.menuOptions[self.menuIndex] == "Leaderboards":
                newState = Leaderboards(self.game)
                newState.nextState()
            if self.menuOptions[self.menuIndex] == "Exit":
                pygame.quit()
                exit()
        self.game.resetKeysPressed()

    def render(self, screen):
        screen.fill((0, 0, 0))
        screen.blit(self.game.menuImage, (0, 0))
        self.game.drawText(screen, "Title", "Never Ending Circles", 
            (255, 255, 255), self.game.wndCenter[0], self.game.wndSize[1]*0.2)
        self.game.drawText(screen, "Main", "Start",
            self.startColor, self.game.wndCenter[0], self.game.wndSize[1]*0.5)
        self.game.drawText(screen, "Main", "Leaderboards",
            self.leaderboardsColor, self.game.wndCenter[0], 
            self.game.wndSize[1]*0.6)
        self.game.drawText(screen, "Main", "Exit",
            self.exitColor, self.game.wndCenter[0], self.game.wndSize[1]*0.7)

    # Updates the menu option being selected
    def updateSelected(self, keysPressed):
        # Allow user to scroll through menu options using arrow keys and
        # menu to be circular
        if keysPressed["up"]:
            self.menuIndex = (self.menuIndex - 1) % len(self.menuOptions)
        elif keysPressed["down"]:
            self.menuIndex = (self.menuIndex + 1) % len(self.menuOptions)
        # Revert to white and change text color to orange if currently selected
        self.startColor = (255, 255, 255)
        self.leaderboardsColor = (255, 255, 255)
        self.exitColor = (255, 255, 255)
        if self.menuIndex == 0:
            self.startColor = (211, 81, 84)
        if self.menuIndex == 1:
            self.leaderboardsColor = (211, 81, 84)
        if self.menuIndex == 2:
            self.exitColor = (211, 81, 84)

# Leaderboards menu
class Leaderboards(GameState):
    def __init__(self, game):
        super().__init__(game)
        self.game = game
        self.menuOptions = ["Level1", "Level2", "Level3", "Level4", "Back"]
        self.menuIndex = 0
        self.level1Color = (211, 81, 84)
        self.level2Color = (255, 255, 255)
        self.level3Color = (255, 255, 255)
        self.level4Color = (255, 255, 255)
        self.backColor = (255, 255, 255)
    
    def update(self, keysPressed):
        self.updateSelected(keysPressed)
        if keysPressed["enter"]:
            if self.menuOptions[self.menuIndex] == "Level1":
                newState = LeaderboardList(self.game, 0)
                newState.nextState()
            if self.menuOptions[self.menuIndex] == "Level2":
                newState = LeaderboardList(self.game, 1)
                newState.nextState()
            if self.menuOptions[self.menuIndex] == "Level3":
                newState = LeaderboardList(self.game, 2)
                newState.nextState()
            if self.menuOptions[self.menuIndex] == "Level4":
                newState = LeaderboardList(self.game, 3)
                newState.nextState()
            if self.menuOptions[self.menuIndex] == "Back":
                self.game.stateStack.pop()
        self.game.resetKeysPressed()

    def render(self, screen):
        screen.fill((0, 0, 0))
        screen.blit(self.game.menuImage, (0, 0))
        self.game.drawText(screen, "Title", "Leaderboards", 
            (255, 255, 255), self.game.wndCenter[0], self.game.wndSize[1]*0.2)
        self.game.drawText(screen, "Main", "Level 1",
            self.level1Color, self.game.wndCenter[0], self.game.wndSize[1]*0.4)
        self.game.drawText(screen, "Main", "Level 2",
            self.level2Color, self.game.wndCenter[0], self.game.wndSize[1]*0.5)
        self.game.drawText(screen, "Main", "Level 3",
            self.level3Color, self.game.wndCenter[0], self.game.wndSize[1]*0.6)
        self.game.drawText(screen, "Main", "Level 4",
            self.level4Color, self.game.wndCenter[0], self.game.wndSize[1]*0.7)
        self.game.drawText(screen, "Main", "Back",
            self.backColor, self.game.wndCenter[0], self.game.wndSize[1]*0.8)

    def updateSelected(self, keysPressed):
        if keysPressed["up"]:
            self.menuIndex = (self.menuIndex - 1) % len(self.menuOptions)
        elif keysPressed["down"]:
            self.menuIndex = (self.menuIndex + 1) % len(self.menuOptions)

        self.level1Color = (255, 255, 255)
        self.level2Color = (255, 255, 255)
        self.level3Color = (255, 255, 255)
        self.level4Color = (255, 255, 255)
        self.backColor = (255, 255, 255)
        if self.menuIndex == 0:
            self.level1Color = (211, 81, 84)
        if self.menuIndex == 1:
            self.level2Color = (211, 81, 84)
        if self.menuIndex == 2:
            self.level3Color = (211, 81, 84)
        if self.menuIndex == 3:
            self.level4Color = (211, 81, 84)
        if self.menuIndex == 4:
            self.backColor = (211, 81, 84)

# Displays the leaderboard scores for a specific level
class LeaderboardList(GameState):
    def __init__(self, game, level):
        super().__init__(game)
        self.game = game
        self.level = level
        self.users = []
        self.scores = []
        # Get users and their scores
        self.getUserScores()
    
    def update(self, keysPressed):
        if keysPressed["enter"]:
            self.game.stateStack.pop()
        self.game.resetKeysPressed()

    def render(self, screen):
        screen.fill((0, 0, 0))
        screen.blit(self.game.menuImage, (0, 0))
        self.game.drawText(screen, "Title", "Level " + str(self.level + 1), 
        (255, 255, 255), self.game.wndCenter[0], self.game.wndSize[1]*0.2)
        # Display the 5 highest score
        for i in range(5):
            # Only display if score is not the default score
            if self.level != self.scores[i]:
                self.game.drawText(screen, "Main", 
                    str(i + 1) + ". " + self.users[i] + ": " + 
                    str(self.scores[i]), (255, 255, 255), 
                    self.game.wndCenter[0], self.game.wndSize[1]*((i + 3) / 10))
        self.game.drawText(screen, "Main", "Back",
            (211, 81, 84), self.game.wndCenter[0], self.game.wndSize[1]*0.9)

    # Get the users and their corresponding scores
    def getUserScores(self):
        users = self.game.server.getUsers()
        scores = []
        # Get the score for each user
        for i in range(len(users)):
            scores += [self.game.server.getUserScore(users[i], self.level)]
        # Sort users and their scores in descending order
        self.users, self.scores = self.bubbleSort(users, scores)
        
    # Sorts scores and makes same changes to users list using bubble sort
    def bubbleSort(self, users, scores):
        # Ceiling index
        endIndex = len(scores) - 1
        # Stops bubble sort when list is already sorted
        sorted = False
        while endIndex >= 0 and not sorted:
            sorted = True
            for i in range(endIndex):
                if scores[i + 1] > scores[i]:
                    temp = scores[i]
                    scores[i] = scores[i + 1]
                    scores[i + 1] = temp
                    temp = users[i]
                    users[i] = users[i + 1]
                    users[i + 1] = temp
                    sorted = False
            endIndex -= 1
        return users, scores

# Level select menu, works exactly like the main menu
class LevelSelect(GameState):
    def __init__(self, game):
        super().__init__(game)
        self.game = game
        self.menuOptions = ["Level1", "Level2", "Level3", "Level4", "Back"]
        self.menuIndex = 0
        self.level1Color = (211, 81, 84)
        self.level2Color = (255, 255, 255)
        self.level3Color = (255, 255, 255)
        self.level4Color = (255, 255, 255)
        self.backColor = (255, 255, 255)
    
    def update(self, keysPressed):
        self.updateSelected(keysPressed)
        if keysPressed["enter"]:
            if self.menuOptions[self.menuIndex] == "Level1":
                # Reset checkpoint related variables when opening a level
                # Prevents carryover of checkpoints after playing other levels
                self.game.resetCheckpointState()
                newState = LevelTransition(self.game, 0)
                newState.nextState()
            if self.menuOptions[self.menuIndex] == "Level2":
                self.game.resetCheckpointState()
                newState = LevelTransition(self.game, 1)
                newState.nextState()
            if self.menuOptions[self.menuIndex] == "Level3":
                self.game.resetCheckpointState()
                newState = LevelTransition(self.game, 2)
                newState.nextState()
            if self.menuOptions[self.menuIndex] == "Level4":
                self.game.resetCheckpointState()
                newState = LevelTransition(self.game, 3)
                newState.nextState()
            if self.menuOptions[self.menuIndex] == "Back":
                self.game.stateStack.pop()
        self.game.resetKeysPressed()

    def render(self, screen):
        screen.fill((0, 0, 0))
        screen.blit(self.game.menuImage, (0, 0))
        self.game.drawText(screen, "Title", "Level Select", 
            (255, 255, 255), self.game.wndCenter[0], self.game.wndSize[1]*0.2)
        self.game.drawText(screen, "Main", "Level 1",
            self.level1Color, self.game.wndCenter[0], self.game.wndSize[1]*0.4)
        self.game.drawText(screen, "Main", "Level 2",
            self.level2Color, self.game.wndCenter[0], self.game.wndSize[1]*0.5)
        self.game.drawText(screen, "Main", "Level 3",
            self.level3Color, self.game.wndCenter[0], self.game.wndSize[1]*0.6)
        self.game.drawText(screen, "Main", "Level 4",
            self.level4Color, self.game.wndCenter[0], self.game.wndSize[1]*0.7)
        self.game.drawText(screen, "Main", "Back",
            self.backColor, self.game.wndCenter[0], self.game.wndSize[1]*0.8)

    def updateSelected(self, keysPressed):
        if keysPressed["up"]:
            self.menuIndex = (self.menuIndex - 1) % len(self.menuOptions)
        elif keysPressed["down"]:
            self.menuIndex = (self.menuIndex + 1) % len(self.menuOptions)

        self.level1Color = (255, 255, 255)
        self.level2Color = (255, 255, 255)
        self.level3Color = (255, 255, 255)
        self.level4Color = (255, 255, 255)
        self.backColor = (255, 255, 255)
        if self.menuIndex == 0:
            self.level1Color = (211, 81, 84)
        if self.menuIndex == 1:
            self.level2Color = (211, 81, 84)
        if self.menuIndex == 2:
            self.level3Color = (211, 81, 84)
        if self.menuIndex == 3:
            self.level4Color = (211, 81, 84)
        if self.menuIndex == 4:
            self.backColor = (211, 81, 84)

# A loading buffer that creates all the tiles and players, and initializes
# starting state of a level
class LevelTransition(GameState):
    def __init__(self, game, level):
        super().__init__(game)
        self.game = game
        # Reset any previously changed level related variables
        self.game.resetLevelState()
        self.game.levels = Levels(self.game.wndCenter, level)
        # Empty tile sprite group to unload any previously played level
        self.game.tiles.empty()
        # Load the level and initialize level related variables
        self.game.tiles, self.game.music, self.game.BPM, backgroundFile, \
        backgroundStartPos, self.game.counterTimer = \
        self.game.levels.loadLevel(self.game.tiles)
        self.game.music = Music(self.game.music, 
            self.game.checkpointMusicTime[-1])
        self.game.background = Background(backgroundFile, backgroundStartPos)
        self.game.camera = Camera(self.game.wndSize)

        # Empty previously loaded players and add again to reset their variables
        self.game.player.empty()
        self.game.player.add(Player("Blue", self.game.wndSize, 
            self.game.FPS, self.game.BPM))
        self.game.player.add(Player("Orange", self.game.wndSize, 
            self.game.FPS, self.game.BPM))

        self.moveToCheckpoint()

    def update(self, keysPressed):
        if keysPressed["enter"]:
            newState = Gameplay(self.game)
            newState.nextState()
        if keysPressed["escape"]:
            newState = PauseMenu(self.game)
            newState.nextState()

    def render(self, screen):
        screen.fill((0, 0, 0))
        screen.blit(self.game.background.image, self.game.background.rect)
        self.game.tiles.draw(screen)
        self.game.player.draw(screen)

    # Checks last checkpoint passed and moves starting position to checkpoint
    def moveToCheckpoint(self):
        # Tracks current tile
        tileCounter = 0
        tilesList = self.game.tiles.sprites()
        # While checkpoint hasn't been reached
        while tileCounter <= self.game.checkpoints[-1]:
            # Center the camera onto the current tile by calculating offset
            self.game.camera.centerCam(tilesList[tileCounter])
            self.game.background.rect.x -= self.game.camera.offset.x / 5
            self.game.background.rect.y -= self.game.camera.offset.y / 5
            # Offset the coordinates of each tile accordingly
            for tile in self.game.tiles.sprites():
                tile.rect.x -= self.game.camera.offset.x
                tile.rect.y -= self.game.camera.offset.y
            tileCounter += 1

# Game state in which the game is being played
class Gameplay(GameState):
    def __init__(self, game):
        super().__init__(game)
        self.game = game
        # Set initial game state to NotStarted
        self.gameState = "NotStarted"
        # Set starting tile and next tile according to latest checkpoint
        self.nextTileIndex = self.game.checkpoints[-1] + 1
        self.startingCheckpoint = self.game.checkpointMusicTime[-1]
        # Used to check if the circle is currently overlapping the tile
        self.passedTile = False
        self.turnedOnInvincible = False
        # Particles list to keep track of all particles
        self.particles = []
        # Initialize score variables
        self.score = self.game.checkpointScore[-1]
        self.scoreType = None
        self.scoreModifier = 1
        self.scoreUpdated = False
        # Initialize music and sound effects
        self.failSound = mixer.Sound("assets/sound/fail.mp3")
        self.musicFile = self.game.music.musicFile
        self.game.music = Music(self.musicFile, 
            self.game.checkpointMusicTime[-1])

    def update(self, keysPressed):
        if self.gameState == "NotStarted":
            # Set the timer of the countdown
            pygame.time.set_timer(pygame.USEREVENT, self.game.counterTimer)
            self.gameState = "Countdown"
        if keysPressed["escape"] and self.gameState != "Countdown":
            # Enter the pause menu
            self.game.music.pause()
            newState = PauseMenu(self.game)
            newState.nextState()
        # If the game has started, update positions and movement of sprites
        if self.gameState != "NotStarted":
            self.game.tiles.update(self.game.screen)
            self.game.player.sprites()[0].update(self.game.player.sprites()[1])
            self.game.player.sprites()[1].update(self.game.player.sprites()[0])
        if keysPressed["r"]:
            # When restarting, stop the music, move back to level select state
            # and reload the level by moving to level transition state
            self.game.music.stopMusic()
            self.game.stateStack.pop()
            self.game.stateStack.pop()
            newState = LevelTransition(self.game, self.game.levels.currentLevel)
            newState.nextState()

        if self.gameState == "Countdown":
            self.countdown()
        if self.gameState == "Gameplay":
            self.gameplay(keysPressed)
        if self.gameState == "Failed":
            self.failed()
        if self.gameState == "Won":
            self.won(keysPressed)
        # Prevents player from just holding down hit keys and winning
        self.game.resetKeysPressed()

    def render(self, screen):
        blueCircle = self.game.player.sprites()[0]
        orangeCircle = self.game.player.sprites()[1]
        screen.fill((0, 0, 0))
        screen.blit(self.game.background.image, self.game.background.rect)
        # Draw the tiles, players and text onto the screen
        self.game.tiles.draw(screen)
        self.game.tiles.update(screen)

        for i in range(30):
            self.particles.append(Particle(self.game))
        for particle in self.particles:
            particle.timer -= 0.4
            pygame.draw.circle(self.game.screen, particle.color, 
            particle.loc, int(particle.timer))
            if particle.timer <= 0:
                self.particles.remove(particle)

        self.game.player.draw(screen)
        self.game.drawText(screen, "Main", "Score: " + str(int(self.score)),
        (255, 255, 255), self.game.wndCenter[0]*0.28, 
        self.game.wndSize[1]*0.08)
        if self.gameState == "Countdown":
            self.game.drawText(screen, "Main", str(self.game.countdownCounter),
            (255, 255, 255), self.game.wndCenter[0], self.game.wndSize[1]*0.25)
        if self.gameState == "Gameplay":
            if self.scoreType != None and self.scoreType == "Perfect" and \
            orangeCircle.moveState == "Fixed":
                self.game.drawText(screen, "Score", self.scoreType,
                (122, 178, 131), orangeCircle.rect.center[0]*0.95, 
                orangeCircle.rect.center[1]*0.93)
            if self.scoreType != None and self.scoreType == "Far" and \
            orangeCircle.moveState == "Fixed":
                self.game.drawText(screen, "Score", self.scoreType,
                (211, 81, 84),  orangeCircle.rect.center[0]*0.95, 
                orangeCircle.rect.center[1]*0.93)
            if self.scoreType != None and self.scoreType == "Perfect" and \
            blueCircle.moveState == "Fixed":
                self.game.drawText(screen, "Score", self.scoreType,
                (122, 178, 131), blueCircle.rect.center[0]*0.95, 
                blueCircle.rect.center[1]*0.93)
            if self.scoreType != None and self.scoreType == "Far" and \
            blueCircle.moveState == "Fixed":
                self.game.drawText(screen, "Score", self.scoreType,
                (211, 81, 84), blueCircle.rect.center[0]*0.95, 
                blueCircle.rect.center[1]*0.93)
        if self.gameState == "Failed":
            self.game.drawText(screen, "Main", "Press r to restart",
            (255, 255, 255), self.game.wndCenter[0], self.game.wndSize[1]*0.25)
            self.game.drawText(screen, "Main", "Score: " + str(int(self.score)),
            (255, 255, 255), self.game.wndCenter[0]*0.28, 
            self.game.wndSize[1]*0.08)
        if self.gameState == "Won":
            self.game.drawText(screen, "Main", "You Won!",
            (255, 255, 255), self.game.wndCenter[0], self.game.wndSize[1]*0.25)
            self.game.drawText(screen, "Main", 
            "Press enter to return to the main menu",
            (255, 255, 255), self.game.wndCenter[0], self.game.wndSize[1]*0.3)
            self.game.drawText(screen, "Main", "Score: " + str(int(self.score)),
            (255, 255, 255), self.game.wndCenter[0]*0.28, 
            self.game.wndSize[1]*0.08)
        if self.scoreUpdated:
            self.game.drawText(screen, "Main", "New highscore updated",
            (255, 255, 255), self.game.wndCenter[0], self.game.wndSize[1]*0.7)


    # Switches game state to gameplay when countdown has reached zero
    def countdown(self):
        if self.game.countdownCounter == 0:
            self.gameState = "Gameplay"
            self.game.music.startMusic()

    # Controls main mechanics of the game
    def gameplay(self, keysPressed):
        # Get blue circle and orange circle sprites
        blueCircle = self.game.player.sprites()[0]
        orangeCircle = self.game.player.sprites()[1]
        # Get next tile and current tile in path
        nextTile = self.game.tiles.sprites()[self.nextTileIndex]
        currentTile = self.game.tiles.sprites()[self.nextTileIndex - 1]

        # Check if the circle is overlapping the tile and game fail condition
        # If the moving circle has collided with the next tile
        if ((pygame.sprite.collide_mask(blueCircle, nextTile) and 
        blueCircle.moveState == "Move") or \
        (pygame.sprite.collide_mask(orangeCircle, nextTile) and
        orangeCircle.moveState == "Move")):
            # Circle is currently overlapping with the tile
            self.passedTile = True
        # If circle has passed over the tile and no longer colliding with tile
        # that means player has failed to press the hit key on time
        elif self.passedTile == True and \
        ((not pygame.sprite.collide_mask(blueCircle, nextTile) and 
        blueCircle.moveState == "Move") or
        (not pygame.sprite.collide_mask(orangeCircle, nextTile) and
        orangeCircle.moveState == "Move")):
            # Play fail sound effect and set the game state to failed
            self.failSound.play()
            self.gameState = "Failed"
            self.game.music.stopMusic()
                
        # If the blue circle is overlaping the tile, "Invincible" mode is on and
        # its coordinates is close to the center of the next tile's center
        if pygame.sprite.collide_mask(blueCircle, nextTile) and \
        self.game.invincible and \
        abs(blueCircle.rect.center[0] - nextTile.rect.center[0]) <= 10 and \
        abs(blueCircle.rect.center[1] - nextTile.rect.center[1]) <= 10:
            # Set score to perfect
            self.scoreType = "Perfect"
            # Score modifier system
            if self.scoreModifier < 1.5:
                self.scoreModifier += 0.05
            self.score += 1000 * self.scoreModifier
            # If next tile has a modifier, update modifier changes to circles
            if nextTile.modifier != "N":
                blueCircle.modifierChanges(nextTile)
                orangeCircle.modifierChanges(nextTile)
            # If next tile is a checkpoint tile and checkpoint has not already
            # been passed
            if nextTile.modifier == "C" and \
            self.game.checkpoints[-1] != self.nextTileIndex - 1:
                # Add checkpoint and current score at passing checkpoint
                self.game.checkpoints.append(self.nextTileIndex)
                self.game.checkpointScore.append(self.score)
            # If current tile is checkpoint tile and music time at checkpoint
            # has not already been added
            if currentTile.modifier == "C" and \
            len(self.game.checkpoints) != len(self.game.checkpointMusicTime):
                # Add current music time so music can be played at
                # appropriate point when starting from the checkpoint
                self.game.checkpointMusicTime.append(self.game.music.getPos())
            # Snap circle to tile, update the center of circular motion
            # of other circle and set the other circle to start moving
            blueCircle.snapToTile(nextTile)
            orangeCircle.moveState = "Move"
            self.nextTileIndex += 1
            # Player has successfully pressed hit button on time
            self.passedTile = False
            self.game.keysPressed["hit"] = False
        # Same as previous, just for orange circle
        elif pygame.sprite.collide_mask(orangeCircle, nextTile) and \
        self.game.invincible and \
        abs(orangeCircle.rect.center[0] - nextTile.rect.center[0]) <= 10 and \
        abs(orangeCircle.rect.center[1] - nextTile.rect.center[1]) <= 10:
            self.scoreType = "Perfect"
            if self.scoreModifier < 1.5:
                self.scoreModifier += 0.05
            self.score += 1000 * self.scoreModifier
            # If next tile has a modifier, update changes to circles
            if nextTile.modifier != "N":
                blueCircle.modifierChanges(nextTile)
                orangeCircle.modifierChanges(nextTile)
            if nextTile.modifier == "C" and \
            self.game.checkpoints[-1] != self.nextTileIndex - 1:
                self.game.checkpoints.append(self.nextTileIndex)
                self.game.checkpointScore.append(self.score)
            if currentTile.modifier == "C" and \
            len(self.game.checkpoints) != len(self.game.checkpointMusicTime):
                self.game.checkpointMusicTime.append(self.game.music.getPos())
            orangeCircle.snapToTile(nextTile)
            blueCircle.moveState = "Move"
            self.nextTileIndex += 1
            self.passedTile = False
            self.game.keysPressed["hit"] = False

        # If circle and tile masks colliding, circle is moving and
        # one of the hit keys were pressed
        elif (pygame.sprite.collide_mask(blueCircle, nextTile) and \
        blueCircle.moveState == "Move" and keysPressed["hit"]):
            # Determine user's score
            self.scoreType = blueCircle.getScore(nextTile)
            if self.scoreType == "Perfect":
                if self.scoreModifier < 1.5:
                    self.scoreModifier += 0.05
                self.score += 1000 * self.scoreModifier
            if self.scoreType == "Far":
                self.scoreModifier = 1
                self.score += 1000
            # If next tile has a modifier, update changes to circles
            if nextTile.modifier != "N":
                blueCircle.modifierChanges(nextTile)
                orangeCircle.modifierChanges(nextTile)
            if nextTile.modifier == "C" and \
            self.game.checkpoints[-1] != self.nextTileIndex - 1:
                self.game.checkpoints.append(self.nextTileIndex)
                self.game.checkpointScore.append(self.score)
            if currentTile.modifier == "C" and \
            len(self.game.checkpoints) != len(self.game.checkpointMusicTime):
                self.game.checkpointMusicTime.append(
                self.startingCheckpoint + self.game.music.getPos())
            blueCircle.snapToTile(nextTile)
            orangeCircle.moveState = "Move"
            self.nextTileIndex += 1
            self.passedTile = False
            self.game.keysPressed["hit"] = False
        elif (pygame.sprite.collide_mask(orangeCircle, nextTile) and
        orangeCircle.moveState == "Move" and keysPressed["hit"]):
            # Determine score
            self.scoreType = orangeCircle.getScore(nextTile)
            if self.scoreType == "Perfect":
                if self.scoreModifier < 1.5:
                    self.scoreModifier += 0.05
                self.score += 1000 * self.scoreModifier
            if self.scoreType == "Far":
                self.scoreModifier = 1
                self.score += 1000
            # If next tile has a modifier, update changes to circles
            if nextTile.modifier != "N":
                blueCircle.modifierChanges(nextTile)
                orangeCircle.modifierChanges(nextTile)
            if nextTile.modifier == "C" and \
            self.game.checkpoints[-1] != self.nextTileIndex - 1:
                self.game.checkpoints.append(self.nextTileIndex)
                self.game.checkpointScore.append(self.score)
            if currentTile.modifier == "C" and \
            len(self.game.checkpoints) != len(self.game.checkpointMusicTime):
                self.game.checkpointMusicTime.append(
                self.startingCheckpoint + self.game.music.getPos())
            orangeCircle.snapToTile(nextTile)
            blueCircle.moveState = "Move"
            self.nextTileIndex += 1
            self.passedTile = False
            self.game.keysPressed["hit"] = False

        # Update camera offset relative to the fixed circle
        if blueCircle.moveState == "Fixed":
            self.game.camera.updateOffset(blueCircle)
        else:
            self.game.camera.updateOffset(orangeCircle)
        self.game.background.rect.x += self.game.camera.offsetdx / 5
        self.game.background.rect.y += self.game.camera.offsetdy / 5
        # Update camera offset and move sprites appropriately
        for sprite in self.game.player.sprites():
            # Move player towards the center of the screen
            sprite.rect.x += self.game.camera.offsetdx
            sprite.rect.y += self.game.camera.offsetdy
        # Go through each tile and offset their positions
        for tile in self.game.tiles.sprites():
            # Move tile towards the center of the screen
            tile.rect.x += self.game.camera.offsetdx
            tile.rect.y += self.game.camera.offsetdy
        for particle in self.particles:
            x = particle.loc[0] + self.game.camera.offsetdx
            y = particle.loc[1] + self.game.camera.offsetdy
            particle.loc = (x, y)
        # Once final tile is reached, set game state to failed
        if self.nextTileIndex == len(self.game.tiles.sprites()):
            if not self.game.turnedOnInvincible:
                self.scoreUpdated = self.game.server.updateUserScore(
                    self.game.username, self.game.levels.currentLevel, 
                    self.score)
            self.gameState = "Won"

    def failed(self):
        self.game.music.stopMusic()

    def won(self, keysPressed):
        blueCircle = self.game.player.sprites()[0]
        orangeCircle = self.game.player.sprites()[1]
        # Update camera offset relative to the fixed circle
        if blueCircle.moveState == "Fixed":
            self.game.camera.updateOffset(blueCircle)
        else:
            self.game.camera.updateOffset(orangeCircle)
        # Update camera offset and move sprites appropriately
        for sprite in self.game.player.sprites():
            # Move player towards the center of the screen
            sprite.rect.x += self.game.camera.offsetdx
            sprite.rect.y += self.game.camera.offsetdy
        # Go through each tile and offset their positions
        for tile in self.game.tiles.sprites():
            # Move tile towards the center of the screen
            tile.rect.x += self.game.camera.offsetdx
            tile.rect.y += self.game.camera.offsetdy

        if keysPressed["enter"]:
            self.game.turnedOnInvincible = False
            self.game.invincible = False
            # Return to main menu
            while len(self.game.stateStack) != 2:
                self.game.stateStack.pop()

class PauseMenu(GameState):
    def __init__(self, game):
        super().__init__(game)
        self.game = game
        self.menuOptions = ["Resume", "Invincible", "ExitToMainMenu"]
        self.menuIndex = 0
        self.resumeColor = (211, 81, 84)
        self.invincibleColor = (255, 255, 255)
        self.exitColor = (255, 255, 255)
    
    def update(self, keysPressed):
        self.updateSelected(keysPressed)
        if keysPressed["enter"]:
            if self.menuOptions[self.menuIndex] == "Resume":
                # Resume game
                self.game.music.unpause()
                self.game.stateStack.pop()
            if self.menuOptions[self.menuIndex] == "Invincible":
                # Toggle invincible mode
                self.game.turnedOnInvincible = True
                if self.game.invincible:
                    self.game.invincible = False
                else:
                    self.game.invincible = True
            if self.menuOptions[self.menuIndex] == "ExitToMainMenu":
                # Return to main menu state
                self.game.resetLevelState()
                self.game.turnedOnInvincible = False
                self.game.invincible = False
                while len(self.game.stateStack) != 2:
                    self.game.stateStack.pop()
        self.game.resetKeysPressed()

    def render(self, screen):
        # Render the gameplay screen
        self.game.stateStack[-2].render(screen)
        self.game.drawText(screen, "Main", "Resume",
            self.resumeColor, self.game.wndCenter[0], self.game.wndSize[1]*0.4)
        if self.game.invincible:
            self.game.drawText(screen, "Main", "Invincible Mode: ON",
                self.invincibleColor, self.game.wndCenter[0], 
                self.game.wndSize[1]*0.6)
        else:
            self.game.drawText(screen, "Main", "Invincible Mode: OFF",
                self.invincibleColor, self.game.wndCenter[0], 
                self.game.wndSize[1]*0.6)
        self.game.drawText(screen, "Main", "Exit to Main Menu",
            self.exitColor, self.game.wndCenter[0], self.game.wndSize[1]*0.7)

    def updateSelected(self, keysPressed):
        if keysPressed["up"]:
            self.menuIndex = (self.menuIndex - 1) % len(self.menuOptions)
        elif keysPressed["down"]:
            self.menuIndex = (self.menuIndex + 1) % len(self.menuOptions)
        
        self.resumeColor = (255, 255, 255)
        self.invincibleColor = (255, 255, 255)
        self.exitColor = (255, 255, 255)
        if self.menuIndex == 0:
            self.resumeColor = (211, 81, 84)
        if self.menuIndex == 1:
            self.invincibleColor = (211, 81, 84)
        if self.menuIndex == 2:
            self.exitColor = (211, 81, 84)