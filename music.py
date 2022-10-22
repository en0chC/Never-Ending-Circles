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
import pygame
#------------------------------------------------------------------------------
from pydub import AudioSegment
from pydub.playback import play
from time import sleep

class Music:
    def __init__(self, musicFile):
        # Start playing background music
        self.musicFile = musicFile
        # Music isn't playing so set state to puased
        self.state = "paused"
        self.piece = AudioSegment.from_wav(musicFile) - 10
        # Start buffer for the countdown at the start of the level
        startBuffer = AudioSegment.from_wav(musicFile)[0:2500] - 1000
        self.piece = startBuffer + self.piece
        self.music = multiprocessing.Process(target=play, args=(self.piece,))

    def stopMusic(self):
        self.music.terminate()
        self.state = "paused"

    def startMusic(self):
        self.music.start()
        self.state = "playing"