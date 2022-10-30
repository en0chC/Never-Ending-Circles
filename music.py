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
import vlc

class Music:
    def __init__(self, musicFile, timePos):
        # Set up music
        self.musicFile = musicFile
        self.timePos = timePos
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        self.music = self.instance.media_new(musicFile)
        self.player.set_media(self.music)
        self.player.audio_set_volume(70)

    def stopMusic(self):
        self.player.stop()

    def startMusic(self):
        self.player.play()
        self.player.set_time(int(self.timePos))

    def pause(self):
        if self.player.is_playing():
            self.player.pause()

    def unpause(self):
        if not self.player.is_playing():
            self.player.pause()

    def getPos(self):
        return self.player.get_time() + 50