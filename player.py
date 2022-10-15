#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# Author : Enoch Luis S Catuncan
# Date Created : October 15th 2022
# version = '1.0'
#------------------------------------------------------------------------------
"""
This module contains the player sprite. The player class takes type, 
windowSize, FPS and RPS as parameters. Type determines whether it is the blue 
or red circle, windowSize is the size of the display window, FPS is the frames 
per second and RPS is the rotations per second.
"""
#------------------------------------------------------------------------------
import math # Used for circular motion of circles
#------------------------------------------------------------------------------
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, type, windowSize, FPS, RPS):
        super().__init__()
        self.type = type
        # (2*math.pi)/FPS to make full rotation in 1 second
        self.rotationPerSecond = ((2*math.pi)/(FPS)) * RPS

        # Set up blue or orange circle image, rect, moveState, angle and
        # center of circular motion
        if type == "Blue":
            self.image = pygame.image.load("assets/images/blue_circle.png")
            self.image = pygame.transform.scale(self.image, (50, 50))
            self.rect = self.image.get_rect(
                center=(windowSize[0] // 2 - 100, windowSize[1] // 2))
            self.moveState = "Move"
            self.angle = (3/2)*math.pi
            self.circMotionCenter = \
                (windowSize[0] // 2, windowSize[1] // 2)
        else:
            self.image = pygame.image.load("assets/images/orange_circle.png")
            self.image = pygame.transform.scale(self.image, (50, 50))
            self.rect = self.image.get_rect(
                center=(windowSize[0] // 2, windowSize[1] // 2))
            self.moveState = "Fixed"
            self.angle = (1/2)*math.pi
            self.circMotionCenter = \
                (windowSize[0] // 2 - 100, windowSize[1] // 2)

    # Moves the circle in circular motion
    def move(self):
        if self.moveState == "Move":
            radius = 100
            self.angle -= self.rotationPerSecond
            if self.angle < 0:
                self.angle = 2*math.pi
            else:
                # Circular motion
                self.rect.center = \
                (self.circMotionCenter[0] + (radius * math.sin(self.angle)),
                self.circMotionCenter[1] + (radius * math.cos(self.angle)))

    # Set center of circular motion and starting position of fixed circle
    def updateCircMotionCenter(self, otherCircle):
        if self.moveState == "Fixed":
            self.circMotionCenter = otherCircle.rect.center
            # Set the starting position of circular motion to opposite
            # the other circle's position
            self.angle = (otherCircle.angle + math.pi) % (2*math.pi)



    def update(self):
        self.move()