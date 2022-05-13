# -*- coding: utf-8 -*-
"""
Created on Thu May 12 17:57:34 2022

@author: ns034983
"""

# Ship Code
import pygame


class Ship:
    def _init_(self, ni_game):
        self.screen = ni_game.screen
        self.screen_rect = ni_game.screen.get_rect()
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom - self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)
