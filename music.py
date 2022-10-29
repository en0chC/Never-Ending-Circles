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
import multiprocessing # Used to allow music be played while game is running
#------------------------------------------------------------------------------
from pydub import AudioSegment
from pydub.playback import play
from pygame import mixer

class Music:
    def __init__(self, musicFile):
        mixer.init()
        # Set up music
        self.musicFile = musicFile
        mixer.music.load(musicFile)
        mixer.music.set_volume(0.3)

    def stopMusic(self):
        mixer.music.stop()

    def startMusic(self):
        mixer.music.play()

    def pause(self):
        mixer.music.pause()

    def unpause(self):
        mixer.music.unpause()