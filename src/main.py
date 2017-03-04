#! /usr/bin/env python

from enum import Enum

import os
import sys
import random

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

            self.fallrate = 4 # 200 pixels per second

            self.score = 0
            self.streak = 0

            self.myfont = pygame.font.SysFont("monospace",40)
            self.boxstack.boxes.append(Box(20))

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
                            box.fall(self.fallrate)

                    if (self.keys[pygame.K_LEFT] or self.keys[pygame.K_a]) and  self.grinch.x >= 20:
                        self.grinch.x -= 8
                    if (self.keys[pygame.K_RIGHT] or self.keys[pygame.K_d]) and self.grinch.y <= self.screen_rect.width - 20 - self.grinch.width:
                        self.grinch.x += 8

        def draw(self):
            self.screen.fill((50, 0, 50))

            if self.mode == Mode.MENU:
                self.screen.blit(self.font.render("Grinch Gets Gifts", True, (255, 255, 255)), (150, 100))
                self.screen.blit(self.font.render("Press space to play!", True, (255, 255, 255)), (150, 500))
            elif self.mode == Mode.INGAME:

                self.screen.blit(pygame.image.load(os.path.join("../res", "background.jpg")).convert(),(0,0))
                self.grinch.draw(self.screen)

                for box in self.boxstack.boxes:
                    box.draw(self.screen)

                string = "Score: " + str(self.score) + " Streak: "+ str(self.streak)
                label = self.myfont.render(string,1,(255,255,0))
                self.screen.blit(label, (self.screen_rect.width - 450,5))

                for box in self.boxstack.boxes:
                        self.screen.blit(box.image,[box.x,box.y])

        def main_loop(self):
            while not self.done:
                self.event_loop()
                self.draw()
                pygame.display.update()

                self.clock.tick(self.fps)
                for box in self.boxstack.boxes:
                    boxRect = pygame.Rect(box.x,box.y, box.width, box.height)
                    grinchRect = pygame.Rect(self.grinch.x,self.grinch.y, self.grinch.width, self.grinch.height)
                    if box.y > self.screen_rect.height:
                        self.boxstack.boxes.pop()
                        self.streak = 0
                        self.boxstack.boxes.append(Box(random.random() * (self.screen_rect.width - 200)))
                        self.fallrate = 4
                    if boxRect.colliderect(grinchRect):
                         self.streak += 1
                         self.score += self.streak
                         self.boxstack.boxes.remove(box)
                         self.boxstack.boxes.append(Box(random.random() * (self.screen_rect.width - 200)))
                         self.fallrate += 0.5

def main():
    Control().main_loop()
    pygame.quit()
    sys.exit()

main()
