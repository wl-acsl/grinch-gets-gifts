#! /usr/bin/env python

from enum import Enum

import os
import sys

import pygame

from grinch import Grinch
from box import Box
from boxstack import BoxStack

class Mode(Enum):
    MENU = 0
    INGAME = 1
    GAMEOVER = 2

class Control(object):
        def __init__(self):
            pygame.init()
            os.environ["SDL_VIDEO_CENTERED"] = "TRUE"
            pygame.display.set_caption("Grinch Gets Gifts")
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.screen_rect = self.screen.get_rect()
            self.done = False
            self.keys = pygame.key.get_pressed()
            self.clock = pygame.time.Clock()
            self.fps = 60.0
            self.mode = Mode.MENU
            self.grinch = Grinch(self.screen_rect.width,self.screen_rect.height)
            self.boxstack = BoxStack()
            self.font = pygame.font.Font(None, 160)

            self.boxstack.boxes.append(Box(0,0,100,200))

            pygame.time.set_timer(pygame.USEREVENT + 1, 20)

        def event_loop(self):
            for event in pygame.event.get():
                self.keys = pygame.key.get_pressed()

                if event.type == pygame.QUIT or self.keys[pygame.K_ESCAPE]:
                    self.done = True

                if self.mode == Mode.MENU and self.keys[pygame.K_SPACE]:
                    self.mode = Mode.INGAME

                if self.mode == Mode.INGAME:
                    if event.type == pygame.USEREVENT + 1:
                        for box in self.boxstack.boxes:
                            box.fall()

                    if self.keys[pygame.K_LEFT] or self.keys[pygame.K_a]:
                        self.grinch.x -= 5
                    if self.keys[pygame.K_RIGHT] or self.keys[pygame.K_d]:
                        self.grinch.x += 5

        def draw(self):
            self.screen.fill((50, 0, 50))

            if self.mode == Mode.MENU:
                self.screen.blit(self.font.render("Grinch Gets Gifts", True, (255, 255, 255)), (150, 100))
                self.screen.blit(self.font.render("Press space to play!", True, (255, 255, 255)), (150, 500))
            elif self.mode == Mode.INGAME:
                self.grinch.draw(self.screen)

                for box in self.boxstack.boxes:
                    box.draw(self.screen)

        def main_loop(self):
            while not self.done:
                self.event_loop()

                self.draw()
                pygame.display.update()

                self.clock.tick(self.fps)
                for box in self.boxstack.boxes:
                    if box.y > self.screen_rect.height:
                        self.boxstack.boxes.pop()
                        print(len(self.boxstack.boxes))

def main():
    Control().main_loop()
    pygame.quit()
    sys.exit()

main()
