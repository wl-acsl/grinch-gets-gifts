#! /usr/bin/env python

from enum import Enum

import os
import sys
import pygame as pg
from grinch import Grinch
from box import Box
from boxstack import BoxStack

class Mode(Enum):
        MENU = 0
        INGAME = 1
        GAMEOVER = 2

class Control(object):
        def __init__(self):
                pg.init()
                os.environ["SDL_VIDEO_CENTERED"] = "TRUE"
                pg.display.set_caption("Grinch Gets Gifts")
                self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
                self.screen_rect = self.screen.get_rect()
                self.done = False
                self.keys = pg.key.get_pressed()
                self.clock = pg.time.Clock()
                self.fps = 60.0
                self.mode = Mode.MENU
                self.grinch = Grinch(self.screen_rect.width,self.screen_rect.height)
                self.boxstack = BoxStack()
                self.fallrate = 2 # 100 pixels per second

                self.boxstack.boxes.append(Box(0,0,100,200))

                pg.time.set_timer(pg.USEREVENT + 1, 20)

        def event_loop(self):
                for event in pg.event.get():
                        self.keys = pg.key.get_pressed()
                        if event.type == pg.QUIT or self.keys[pg.K_ESCAPE]:
                                self.done = True
                        if event.type == pg.USEREVENT + 1:
                                for box in self.boxstack.boxes:
                                        box.y += self.fallrate

        def draw(self):
                self.screen.fill((50, 60, 50))

                if self.mode == Mode.MENU:
                        self.screen.fill((50, 0, 50))

                self.screen.blit(self.grinch.image,[self.grinch.x,self.grinch.y])

                for box in self.boxstack.boxes:
                    box.draw(self.screen)

        def main_loop(self):
                while not self.done:
                        self.event_loop()
                        self.draw()
                        pg.display.update()
                        self.clock.tick(self.fps)
                        for box in self.boxstack.boxes:
                                if box.y > self.screen_rect.height:
                                        self.boxstack.boxes.pop()
                                        print(len(self.boxstack.boxes))

def main():
        Control().main_loop()
        pg.quit()
        sys.exit()

main()
