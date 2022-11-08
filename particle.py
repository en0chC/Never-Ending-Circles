#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# Author : Enoch Luis S Catuncan
# Date Created : November 8th 2022
#------------------------------------------------------------------------------
"""
This module contains the Particle class which defines a single particle for use
in particle effects.
"""
#------------------------------------------------------------------------------
from random import randint
#------------------------------------------------------------------------------

class Particle:
    def __init__(self, game):
        blueCircle = game.player.sprites()[0]
        orangeCircle = game.player.sprites()[1]
        # Place the particle at whichever circle is moving and 
        # set its color accordingly
        if blueCircle.moveState == "Move":
            x = blueCircle.rect.center[0] + randint(-10, 10)
            y = blueCircle.rect.center[1] + randint(-10, 10)
            self.loc = (x, y)
            self.color = (4, 17, 193)
        if orangeCircle.moveState == "Move":
            x = orangeCircle.rect.center[0] + randint(-10, 10)
            y = orangeCircle.rect.center[1] + randint(-10, 10)
            self.loc = (x, y)
            self.color = (219, 21, 1)
        # Timer for how long the particle lasts
        self.timer = 8