#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# Author : Enoch Luis S Catuncan
# Date Created : October 22nd 2022
# version = '1.0'
#------------------------------------------------------------------------------
"""
This module contains the Levels class which contains the different levels in 
the game.
"""
#------------------------------------------------------------------------------
import pygame
#------------------------------------------------------------------------------
from tile import Tile

class Levels:
    def __init__(self, wndCenter):
        self.wndCenter = wndCenter

        # Levels consist of music file name, BPM and level tiles
        self.level1 = [
            "assets/music/level1.wav", 100,
            "30WtoE", "01WtoS", "01NtoE", "14WtoE", "01WtoS", "01NtoE", 
            "14WtoE", "01WtoS", "01NtoE", "14WtoE", "01WtoN", "01StoE", 
            "14WtoE", "01WtoN", "01StoE", "12WtoE", "01WtoN", "01StoE", 
            "01WtoN", "01StoE", "08WtoE", "01WtoS", "01NtoE", "01WtoS", 
            "01NtoE", "01WtoS", "01NtoE", "01WtoS", "01NtoE", "12WtoE", 
            "01WtoN", "01StoE", "01WtoN", "01StoE", "08WtoE", "01WtoS", 
            "01NtoE", "01WtoS", "01NtoE", "02WtoE", "01WtoN", "01StoE", 
            "07WtoE"
        ]
        # Stores all the level arrays
        self.levels = [self.level1]
        # Current level corresponding to level's index in levels array
        self.currentLevel = 0
    
    def loadLevel(self, tiles):
        # Create tiles sprite group
        tiles.empty()
        self.nextTileCenter = [0,0]

        # Go through each tile in level array
        for tile in self.levels[self.currentLevel][2:]:
            for i in range(int(tile[0:2])):
                tiles.add(Tile(self.wndCenter, self.nextTileCenter, tile[2:]))

                # Get ending direction from tile and set next tile center to
                # the next spot in corresponding direction
                if tile.split("to")[1] == "N":
                    self.nextTileCenter[1] += -100
                if tile.split("to")[1] == "E":
                    self.nextTileCenter[0] += 100
                if tile.split("to")[1] == "S":
                    self.nextTileCenter[1] += 100
                if tile.split("to")[1] == "W":
                    self.nextTileCenter[0] += -100

        # Return tiles sprite group and BPM of the level
        return tiles, self.levels[self.currentLevel][0], \
        self.levels[self.currentLevel][1]