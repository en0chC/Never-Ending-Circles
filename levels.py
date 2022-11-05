#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# Author : Enoch Luis S Catuncan
# Date Created : October 22nd 2022
#------------------------------------------------------------------------------
"""
This module contains the Levels class which contains the different levels in 
the game. Format of tiles in level array is '[Modifier][Number of tiles]
[FromDirection]to[ToDirection]', each section with length "[1][2][1-2]to[1-2]" 
If the modifier is S 'Change speed', format is 
'[Modifier][Number of tiles][New BPM][FromDirection]to[ToDirection]' each 
section with length "[1][2][6][1-2]to[1-2]". The different modifiers are 
'N' - 'Normal tile', 'S' - 'Change speed/BPM', 'R' - 'Reverse direction' and 
'C' - 'Checkpoint tile'.
"""
#------------------------------------------------------------------------------
from tile import Tile

class Levels:
    def __init__(self, wndCenter, currentLevel):
        self.wndCenter = wndCenter
        self.currentLevel = currentLevel
        # Levels consist of music file name, BPM and level tiles
        self.level1 = [
            "assets/music/level1.mp3", 124.3, 
            "assets/images/backgrounds/world1.jpg", 250,
            "N31WtoE", "N01WtoS", "N01NtoE", "N14WtoE", "N01WtoS", "N01NtoE", 
            "N14WtoE", "N01WtoS", "N01NtoE", "N14WtoE", "N01WtoN", "N01StoE", 
            "N14WtoE", "N01WtoN", "N01StoE", "N05WtoE", "C01WtoE", "N06WtoE", 
            "N01WtoN", "N01StoE", "N01WtoN", "N01StoE", "N08WtoE", "N01WtoS", 
            "N01NtoE", "N01WtoS", "N01NtoE", "N01WtoS", "N01NtoE", "N01WtoS", 
            "N01NtoE", "N12WtoE", "N01WtoN", "N01StoE", "N01WtoN", "N01StoE", 
            "R08WtoE", "N01WtoS", "N01NtoE", "N01WtoS", "N01NtoE", "N02WtoE", 
            "N01WtoN", "N01StoE", "S01031.00WtoE", "N06WtoE"
        ]
        self.level2 = [
            "assets/music/level2.mp3", 149.5,
            "assets/images/backgrounds/world2.jpg", 0,
            "N29WtoE", "N01WtoS", "N01NtoW", "N07EtoW", "N01EtoS", "N01NtoE",
            "N05WtoE", "N01WtoS", "N01NtoW", "N07EtoW", "N01EtoS", "N01NtoE",
            "N09WtoE", "N01WtoS", "N01NtoW", "N01EtoS", "N01NtoE", "N01WtoS", 
            "N01NtoW", "N01EtoS", "N01NtoE", "N01WtoS", "N01NtoW", "N01EtoS", 
            "N01NtoE", "N04WtoE", "N01WtoS", "N01NtoW", "N01EtoS", "N01NtoE",
            "N01WtoS", "N01NtoW", "N01EtoS", "N01NtoE", "N01WtoS", "N01NtoW", 
            "N01EtoS", "N01NtoE", "N04WtoE", "N01WtoN", "N01StoE", "N01WtoS", 
            "N01NtoE", "N01WtoN", "N01StoE", "N01WtoS", "N01NtoE", "N01WtoN", 
            "N01StoE", "N01WtoS", "N01NtoE", "N01WtoN", "N01StoE", "N01WtoS", 
            "N01NtoE", "N01WtoN", "N01StoE", "N01WtoS", "N01NtoE", "N01WtoN", 
            "N01StoE", "N01WtoS", "N01NtoE", "N01WtoN", "N01StoE", "N11WtoE",
            "N01WtoS", "N01NtoW", "N01EtoS", "N01NtoE", "N04WtoE", "N01WtoS", 
            "N01NtoW", "N01EtoS", "N01NtoE", "N04WtoE", "N01WtoS", "N01NtoW", 
            "N01EtoS", "N01NtoE", "N04WtoE", "N01WtoS", "N01NtoW", "N01EtoS", 
            "N01NtoE", "N01WtoE", "N01WtoN", "N01StoE", "N01WtoE", "N01WtoS", 
            "N01NtoW", "N01EtoS", "N01NtoE", "N01WtoE", "N01WtoN", "N01StoE", 
            "N01WtoE", "N01WtoS", "N01NtoW", "N01EtoS", "N01NtoE", "N01WtoE", 
            "N01WtoN", "N01StoE", "N01WtoE", "N01WtoS", "N01NtoW", "N01EtoS", 
            "N01NtoE", "N01WtoE", "N01WtoN", "N01StoE", "N01WtoE", "N01WtoS",
            "N01NtoW", "N01EtoW"
        ]
        # Stores all the level arrays
        self.levels = [self.level1, self.level2]
        # Keep track of where the next tile should be placed
        self.nextTileCenter = [0,0]

    def loadLevel(self, tiles):
        self.nextTileCenter = [0,0]
        self.currentBPM = self.levels[self.currentLevel][1]
        # Go through each tile in level array
        for tile in self.levels[self.currentLevel][4:]:
            for i in range(int(tile[1:3])):
                # If normal tile
                if tile[0] == "N":
                    tiles.add(Tile(self.wndCenter, self.nextTileCenter, 
                    tile[3:], tile[0], self.currentBPM))
                # If change speed tile
                if tile[0] == "S":
                    tiles.add(Tile(self.wndCenter, self.nextTileCenter, 
                    tile[9:], tile[0:9], self.currentBPM))
                    self.currentBPM = float(tile[3:9])
                # If reverse direction tile
                if tile[0] == "R":
                    tiles.add(Tile(self.wndCenter, self.nextTileCenter, 
                    tile[3:], tile[0], self.currentBPM))
                if tile[0] == "C":
                    tiles.add(Tile(self.wndCenter, self.nextTileCenter, 
                    tile[3:], tile[0], self.currentBPM))
                # Get ending direction from tile and set next tile center 
                # to the next spot in corresponding direction
                if tile.split("to")[1] == "N":
                    self.nextTileCenter[1] += -100
                if tile.split("to")[1] == "E":
                    self.nextTileCenter[0] += 100
                if tile.split("to")[1] == "S":
                    self.nextTileCenter[1] += 100
                if tile.split("to")[1] == "W":
                    self.nextTileCenter[0] += -100

        # Return tiles sprite group, music file, BPM of the level, background
        # file and starting position of the background
        return tiles, self.levels[self.currentLevel][0], \
        self.levels[self.currentLevel][1], self.levels[self.currentLevel][2], \
        self.levels[self.currentLevel][3]