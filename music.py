#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# Author : Enoch Luis S Catuncan
# Date Created : October 22nd 2022
#------------------------------------------------------------------------------
"""
This module contains the Music class that is in charge of playing the music
in the levels. Class takes musicFile, file path to music file and timePos, 
time in the music file from which to start from.
"""
#------------------------------------------------------------------------------
import vlc

class Music:
    def __init__(self, musicFile, timePos):
        # Set up music
        self.musicFile = musicFile
        self.timePos = timePos
        # Set up vlc player
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        self.music = self.instance.media_new(musicFile)
        self.player.set_media(self.music)
        self.player.audio_set_volume(70)

    def stopMusic(self):
        self.player.stop()

    def startMusic(self):
        self.player.play()
        # Move to starting time
        self.player.set_time(int(self.timePos))

    def pause(self):
        if self.player.is_playing():
            self.player.pause()

    def unpause(self):
        if not self.player.is_playing():
            self.player.pause()

    def getPos(self):
        return self.player.get_time() + 50