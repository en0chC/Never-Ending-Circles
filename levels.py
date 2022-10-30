#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# Author : Enoch Luis S Catuncan
# Date Created : October 22nd 2022
# version = '1.0'
#------------------------------------------------------------------------------
"""
This module contains the Levels class which contains the different levels in 
the game. Format of tiles in level array is '[Modifier][Number of tiles]
[FromDirection]to[ToDirection]' If the modifier is S 'Change speed', format is 
'[Modifier][Number of tiles][New BPM][FromDirection]to[ToDirection]'. The
different modifiers are 'N' - 'Normal tile', 'S' - 'Change speed/BPM', 'R' - 
'Reverse direction' and 'C' - 'Checkpoint tile'.
"""
#------------------------------------------------------------------------------
from tile import Tile

class Levels:
    def __init__(self, wndCenter):
        self.wndCenter = wndCenter

        # Levels consist of music file name, BPM and level tiles
        self.level1 = [
            "assets/music/level1.mp3", 124.3,
            "N31WtoE", "N01WtoS", "N01NtoE", "N14WtoE", "N01WtoS", "N01NtoE", 
            "N14WtoE", "N01WtoS", "N01NtoE", "N14WtoE", "N01WtoN", "N01StoE", 
            "N14WtoE", "N01WtoN", "N01StoE", "N05WtoE", "C01WtoE", "N06WtoE", 
            "N01WtoN", "N01StoE", "N01WtoN", "N01StoE", "N08WtoE", "N01WtoS", 
            "N01NtoE", "N01WtoS", "N01NtoE", "N01WtoS", "N01NtoE", "N01WtoS", 
            "N01NtoE", "N12WtoE", "N01WtoN", "N01StoE", "N01WtoN", "N01StoE", 
            "R08WtoE", "N01WtoS", "N01NtoE", "N01WtoS", "N01NtoE", "N02WtoE", 
            "N01WtoN", "N01StoE", "S01030.00WtoE", "N06WtoE"
        ]

        # Stores all the level arrays
        self.levels = [self.level1]
    
    def loadLevel(self, tiles, currentLevel):
        # Create tiles sprite group
        self.nextTileCenter = [0,0]
        self.currentBPM = self.levels[currentLevel][1]

        # Go through each tile in level array
        for tile in self.levels[currentLevel][2:]:
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

        # Return tiles sprite group and BPM of the level
        return tiles, self.levels[currentLevel][0], \
        self.levels[currentLevel][1]