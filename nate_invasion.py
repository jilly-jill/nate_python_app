# -*- coding: utf-8 -*-
"""
Created on Thu May 12 17:55:06 2022

@author: ns034983
"""

# Project Code
import sys
from settings import Settings
from ship import Ship
import pygame;


class nate_invasion:

    # initialize game settings and background design

    def _init_(self):
        pygame.get_init();
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (
                self.settings.screen_width,
                self.settings.screen_height)
        )
        pygame.display.set_caption("Nate Invasion")
        self.ship = Ship(self)

    # Run Game
    def run_game(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    False;
                    sys.exit();
                else:
                    True;



if nate_invasion == 'Main':
    ni = nate_invasion()
    ni.run_game()
