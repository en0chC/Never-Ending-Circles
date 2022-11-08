#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# Author : Enoch Luis S Catuncan
# Date Created : October 15th 2022
#------------------------------------------------------------------------------
"""
This module is the python file that will be run to start the game.
"""
#------------------------------------------------------------------------------
from neverEndingCircles import NeverEndingCircles

if __name__ == "__main__":
    neverEndingCircles = NeverEndingCircles()
    neverEndingCircles.mainLoop()