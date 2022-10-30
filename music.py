#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# Author : Enoch Luis S Catuncan
# Date Created : October 22nd 2022
# version = '1.0'
#------------------------------------------------------------------------------
"""
This module contains the Music class that is in charge of playing the music
in the levels.
"""
#------------------------------------------------------------------------------
from pygame import mixer

class Music:
    def __init__(self, musicFile, timePos):
        mixer.init()
        # Set up music
        self.musicFile = musicFile
        self.timePos = timePos
        mixer.music.load(musicFile)
        mixer.music.set_volume(0.3)

    def stopMusic(self):
        mixer.music.stop()

    def startMusic(self):
        mixer.music.play(0, self.timePos)

    def pause(self):
        mixer.music.pause()

    def unpause(self):
        mixer.music.unpause()

    def getPos(self):
        return mixer.music.get_pos() / 1000