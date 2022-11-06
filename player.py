#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# Author : Enoch Luis S Catuncan
# Date Created : October 15th 2022
#------------------------------------------------------------------------------
"""
This module contains the Player sprite. The player class takes type, 
windowSize, FPS and BPM as parameters. Type determines whether it is the blue 
or red circle, windowSize is the size of the display window, FPS is the frames 
per second and BPM is the Beats Per Minute.
"""
#------------------------------------------------------------------------------
import math # Used for circular motion of circles
#------------------------------------------------------------------------------
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, type, windowSize, FPS, BPM):
        super().__init__()
        # Set up blue or orange circle sprite
        if type == "Blue":
            self.image = pygame.image.load(
                "assets/images/blue_circle.png").convert_alpha()
            self.rect = self.image.get_rect(
                center=(windowSize[0]//2 + 100, windowSize[1]//2))
            self.moveState = "Move"
            # Set starting position of circular motion to right
            self.angle = (1/2)*math.pi
            # Set center of circular motion to center of other circle
            self.circMotionCenter = (windowSize[0]//2, windowSize[1]//2)
        else:
            self.image = pygame.image.load(
                "assets/images/orange_circle.png").convert_alpha()
            self.rect = self.image.get_rect(
                center=(windowSize[0]//2, windowSize[1]//2))
            self.moveState = "Fixed"
            # Set starting position of circular motion to left
            self.angle = (3/2)*math.pi
            # Set center of circular motion to center of other circle
            self.circMotionCenter = (windowSize[0]//2 + 100, windowSize[1]//2)
        self.radius = 100
        # (2*math.pi)/FPS to make full rotation in 1 second
        # Around 1 rotation for 100 BPM
        # Positive rotationPerSecond is clockwise rotation
        self.FPS = FPS
        self.rotationPerSecond = ((2*math.pi)/(self.FPS)) * (BPM/100)
        # Set up mask for collision detection
        self.mask = pygame.mask.from_surface(self.image)
        
    # Moves the circle in circular motion
    def move(self):
        if self.moveState == "Move":
            # Clockwise movement by reducing angle
            # Anti-clockwise movement by increasing angle
            self.angle -= self.rotationPerSecond
            # Uniform circular motion
            self.rect.center = \
            (self.circMotionCenter[0] + (self.radius*math.sin(self.angle)),
            self.circMotionCenter[1] + (self.radius*math.cos(self.angle)))

    # Snaps the moving circle to the next tile
    def snapToTile(self, nextTile):
        # Distance from current center to tile center using pythagorean theorem 
        distanceToTile = \
        ((nextTile.rect.center[1] - self.rect.center[1])**2 
        + (nextTile.rect.center[0] - self.rect.center[0])**2)**(1/2)
        # Calculate change in angle using SOHCAHTOA and set new angle
        self.angle = (self.angle - 2*math.asin(distanceToTile/(2*self.radius)) 
        % (2*math.pi))
        # Place the circle on the middle of the tile
        self.rect.center = nextTile.rect.center
        self.moveState = "Fixed"

    # Calculates score
    def getScore(self, nextTile):
        # Calculate distance from circle's center to tile center
        distanceToTile = \
        ((nextTile.rect.center[1] - self.rect.center[1])**2 
        + (nextTile.rect.center[0] - self.rect.center[0])**2)**(1/2)
        # Score system
        if distanceToTile <= 24:
            return "Perfect"
        else:
            return "Far"

    # For the fixed player, update center of circular motion and 
    # starting position of the circular motion relative to moving circle
    def updateCircularMotionCenter(self, otherCircle):
        self.circMotionCenter = otherCircle.rect.center
        if self.moveState == "Fixed":
            # Set the starting circular position of fixed circle to opposite
            # the other circle's circular position
            self.angle = (otherCircle.angle + math.pi)

    # Update circle properties if there is a modifier tile
    def modifierChanges(self, nextTile):
        # If modifier tile is speed change
        if nextTile.modifier == "S":
            # Calculate new rotations per second
            if self.rotationPerSecond < 0:
                self.rotationPerSecond = -(((2*math.pi)/(self.FPS)) 
                * (nextTile.modifierBPM/100))
            else:
                self.rotationPerSecond = (((2*math.pi)/(self.FPS)) 
                * (nextTile.modifierBPM/100))
        # If modifier tile is reverse direction
        if nextTile.modifier == "R":
            # Reverse direction of rotation
            self.rotationPerSecond = -self.rotationPerSecond

    # Updates circular movement of circle
    def update(self, otherCircle):
        self.move()
        self.updateCircularMotionCenter(otherCircle)