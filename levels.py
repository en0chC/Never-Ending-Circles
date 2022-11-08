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
#------------------------------------------------------------------------------

class Levels:
    def __init__(self, wndCenter, currentLevel):
        self.wndCenter = wndCenter
        self.currentLevel = currentLevel
        # Levels consist of music file name, BPM, background file, 
        # background offset, countdown timer and sequence of level tiles
        self.level1 = [
            "assets/music/level1.mp3", 124, 
            "assets/images/backgrounds/world1.jpg", (0, 250),
            750,
            "N31WtoE", "N01WtoS", "N01NtoE", "N14WtoE", "N01WtoS", "N01NtoE", 
            "N14WtoE", "N01WtoS", "N01NtoE", "N14WtoE", "N01WtoN", "N01StoE", 
            "N14WtoE", "N01WtoN", "N01StoE", "N12WtoE", 
            "N01WtoN", "N01StoE", "N01WtoN", "N01StoE", "N08WtoE", "N01WtoS", 
            "N01NtoE", "N01WtoS", "N01NtoE", "N01WtoS", "N01NtoE", "N01WtoS", 
            "N01NtoE", "N12WtoE", "N01WtoN", "N01StoE", "N01WtoN", "N01StoE", 
            "N03WtoE", "R02WtoE", "N03WtoE", "N01WtoS", "N01NtoE", "N01WtoS", 
            "N01NtoE", "N02WtoE", "N01WtoN", "N01StoE", "S01031.00WtoE", 
            "N06WtoE"
        ]
        self.level2 = [
            "assets/music/level2.mp3", 69.5,
            "assets/images/backgrounds/world2.jpg", (1000, 1800),
            900,
            "N01WtoE", "N01WtoNE", "N01SWtoE", "N02WtoE", "N01WtoNE", 
            "N01SWtoE", "N02WtoE", "N01WtoNE", "N01SWtoE", "N02WtoE", 
            "N01WtoNE", "N01SWtoE", "N02WtoE",
            "N01WtoNE", "N01SWtoN", "N01StoE", 
            "N01WtoE", "N01WtoNE", "N01SWtoN", "N01StoE", "N01WtoE", 
            "N01WtoNE", "N01SWtoN", "N01StoE", "N01WtoE", "N01WtoNE",
            "N01SWtoN", "N01StoE", "N02WtoE", "N01WtoNE", "N01SWtoN", 
            "N01StoW", "N01EtoW", "R01EtoW", "N01EtoNW", "N01SEtoN", "N01StoE", 
            "N01WtoE", "R01WtoE", "N01WtoNE", "N01SWtoN", "N01StoW", "N01EtoW", 
            "R01EtoW", "N01EtoNW", "N01SEtoN", "N01StoE", "N01WtoE", "R01WtoE", 
            "N01WtoNE","N01SWtoN", "N01StoW", "N01EtoW", "R01EtoW", "N01EtoNW", 
            "N01SEtoN", "N01StoE", "N01WtoE", "R01WtoE", "N01WtoNE", 
            "N01SWtoN", "N01StoW", "N01EtoW", "R01EtoW", "N01EtoNW", 
            "N01SEtoN", "N01StoW", "N01EtoW", "N01EtoNE", "N01SWtoSE", 
            "N01NWtoS", "N01NtoW", "N02EtoW", "N01EtoNE", "N01SWtoSE", 
            "N01NWtoS", "N01NtoW", "N02EtoW", "N01EtoNE", "N01SWtoSE", 
            "N01NWtoS", "N01NtoW", "N02EtoW", "N01EtoNE", "N01SWtoSE", 
            "N01NWtoS", "N01NtoW", "N02EtoW", "N01EtoNE", "N01SWtoSE", 
            "N01NWtoS", "N01NtoW", "N02EtoW", "N01EtoNE", "N01SWtoSE", 
            "N01NWtoS", "N01NtoW", "N02EtoW", "N01EtoNE", "N01SWtoSE", 
            "N01NWtoS", "N01NtoW", "N02EtoW", "N01EtoNE", "N01SWtoSE", 
            "N01NWtoS", "N01NtoW", "N01EtoW", "S01017.50EtoW", "N03EtoW", 
            "S01034.30EtoS", "N01NtoW", "N01EtoS", "N01NtoW", "N02EtoW", 
            "S01069.60EtoW", "N04EtoW", "N01EtoNW", "N01SEtoW", "N02EtoW", 
            "N01EtoNW", "N01SEtoN", "N01StoE", "N01WtoE", "R01WtoE", 
            "N01WtoNE", "N01SWtoN", "N01StoW", "N01EtoW", "R01EtoW",
            "N01EtoNW", "N01SEtoN", "N01StoE", "N01WtoS", "N01NtoW", "N01EtoW",
            "N01EtoNW", "N01SEtoW", "N02EtoW", "N01EtoNW", "N01SEtoW", 
            "N02EtoW", "N01EtoNW", "N01SEtoN", "N01StoE", "N01WtoE", "R01WtoE",
            "N01WtoNE", "N01SWtoE", "N01WtoN", "N01StoW", "N01EtoW"
        ]
        self.level3 = [
            "assets/music/level3.mp3", 149.7,
            "assets/images/backgrounds/world3.jpg", (0, 0),
            600,
            "N29WtoE", "N01WtoS", "N01NtoW", "N07EtoW", "N01EtoS", "N01NtoE",
            "N05WtoE", "N01WtoS", "N01NtoW", "N07EtoW", "N01EtoS", "N01NtoE",
            "N09WtoE", "N01WtoS", "N01NtoW", "N01EtoS", "N01NtoE", "N01WtoS", 
            "N01NtoW", "N01EtoS", "N01NtoE", "N01WtoS", "N01NtoW", "N01EtoS", 
            "N01NtoE", 
            "N02WtoE", "C01WtoE", "N01WtoE",
            "N01WtoS", "N01NtoW", "N01EtoS", "N01NtoE",
            "N01WtoS", "N01NtoW", "N01EtoS", "N01NtoE", "N01WtoS", "N01NtoW", 
            "N01EtoS", "N01NtoE", "N04WtoE", "N01WtoN", "N01StoE", "N01WtoS", 
            "N01NtoE", "N01WtoN", "N01StoE", "N01WtoS", "N01NtoE", "N01WtoN", 
            "N01StoE", "N01WtoS", "N01NtoE", "N01WtoN", "N01StoE", "N01WtoS", 
            "N01NtoE", "N01WtoN", "N01StoE", "N01WtoS", "N01NtoE", "N01WtoN", 
            "N01StoE", "N01WtoS", "N01NtoE", "N01WtoN", "N01StoE", 
            "N05WtoE", "C01WtoE", "N05WtoE",
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
        self.level4 = [
            "assets/music/level4.mp3", 131.8,
            "assets/images/backgrounds/world4.jpg", (400, 0),
            670,
            "N01WtoE", "N01WtoS", "N01NtoW", "R01EtoS", "N01NtoE", "N02WtoE",
            "R01WtoS", "N01NtoW", "R01EtoS", "N01NtoE", "N02WtoE", "R01WtoS",
            "N01NtoW", "R01EtoS", "N01NtoE", "N01WtoE", "N01WtoS", "N01NtoW",
            "N01EtoS", "N01NtoE", "R01WtoS", "N01NtoW", "N01EtoS", "N01NtoW",
            "N06EtoW", "N01EtoN", "N01StoE", "N01WtoS", "N01NtoW", "N06EtoW",
            "N01EtoN", "N01StoE", "N01WtoS", "N01NtoW", "N03EtoW", "N01EtoS", 
            "N01NtoE", "N01WtoN", "N01StoW", "N03EtoW", "N01EtoS", "N01NtoE", 
            "N01WtoN", "N01StoW", "N03EtoW", "N01EtoS", "N02NtoS", "N01NtoE",
            "N03WtoE", "S01044.00WtoE", "S01132.10WtoE", "N05WtoE", "N01WtoS",
            "N01NtoW", "R01EtoS", "N01NtoE", "N06WtoE", "R01WtoS", "N01NtoW",
            "R01EtoS", "N01NtoE", "N01WtoE", "N01WtoS", "N01NtoW", "N01EtoN", 
            "N01StoE", "N04WtoE", "N01WtoS", "N01NtoW", "N01EtoN", "N01StoE", 
            "N03WtoE", "N01WtoS", "N01NtoW", "N01EtoN", "N01StoE", "N01WtoS",
            "N03NtoS", "N01NtoW", "N01EtoN", "N01StoE", "N01WtoS", "N01NtoS",
            "N01NtoW", "S01044.00EtoW", "S01131.80EtoS", "N01NtoE", "R01WtoS",
            "N01NtoW", "N01EtoW", "N01EtoS", "N01NtoE", "N01WtoS", "N01NtoW",
            "R01EtoS", "N01NtoE", "N01WtoE", "N01WtoS", "N01NtoW", "N01EtoS",
            "N01NtoE", "R01WtoS", "N01NtoW", "N01EtoW", "N01EtoS", "N01NtoE",
            "N01WtoS", "N01NtoW", "R01EtoS", "N01NtoE", "N01WtoS", "N01NtoE",
            "R01WtoS", "N01NtoW", "R01EtoS", "N01NtoE", "N01WtoE", "N01WtoS",
            "N01NtoW", "N01EtoS", "N01NtoE", "R01WtoS", "N01NtoW", "N01EtoW",
            "N01EtoS", "N01NtoE", "N01WtoS", "N01NtoW", "R01EtoS", "N01NtoE",
            "N01WtoE", "N01WtoS", "N01NtoW", "N01EtoS", "N01NtoE", "R01WtoS",
            "N01NtoW", "N02EtoW", "N01EtoN", "N01StoE", "N01WtoS", "N02NtoS",
            "N01NtoW", "N01EtoN", "N01StoE", "N01WtoS", "N01NtoS", "N01NtoW",
            "N03EtoW", "N01EtoN", "N01StoE", "R01WtoN", "N01StoW", "R01EtoN",
            "N01StoE", "N01WtoE"
        ]
        # Stores all the level arrays
        self.levels = [self.level1, self.level2, self.level3, self.level4]
        # Keep track of where the next tile should be placed
        self.nextTileCenter = [0,0]

    def loadLevel(self, tiles):
        self.nextTileCenter = [0,0]
        self.currentBPM = self.levels[self.currentLevel][1]
        # Go through each tile in level array
        for tile in self.levels[self.currentLevel][5:]:
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

                # Tiles going diagonally
                if tile.split("to")[0][-2] == "NE" or \
                tile.split("to")[0][-2] == "NW" or \
                tile.split("to")[0][-2] == "SE" or \
                tile.split("to")[0][-2] == "SW":
                    if tile.split("to")[1] == "NE":
                        self.nextTileCenter[0] += 120
                        self.nextTileCenter[1] -= 120
                    if tile.split("to")[1] == "NW":
                        self.nextTileCenter[0] -= 120
                        self.nextTileCenter[1] -= 120
                    if tile.split("to")[1] == "SE":
                        self.nextTileCenter[0] += 120
                        self.nextTileCenter[1] += 120
                    if tile.split("to")[1] == "SW":
                        self.nextTileCenter[0] -= 120
                        self.nextTileCenter[1] += 120
                else:
                    if tile.split("to")[1] == "NE":
                        self.nextTileCenter[0] += 70
                        self.nextTileCenter[1] -= 70
                    if tile.split("to")[1] == "NW":
                        self.nextTileCenter[0] -= 70
                        self.nextTileCenter[1] -= 70
                    if tile.split("to")[1] == "SE":
                        self.nextTileCenter[0] += 70
                        self.nextTileCenter[1] += 70
                    if tile.split("to")[1] == "SW":
                        self.nextTileCenter[0] -= 70
                        self.nextTileCenter[1] += 70

        # Return tiles sprite group, music file, BPM of the level, background
        # file, starting position of the background and countdown time
        return tiles, self.levels[self.currentLevel][0], \
        self.levels[self.currentLevel][1], self.levels[self.currentLevel][2], \
        self.levels[self.currentLevel][3], self.levels[self.currentLevel][4]