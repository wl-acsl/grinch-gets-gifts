#! /usr/bin/env python

import os
import sys
import pygame as pg

class Control(object):
    def __init__(self):
        pg.init()
        os.environ["SDL_VIDEO_CENTERED"] = "TRUE"
        pg.display.set_caption("Grinch Gets Gifts")
        self.screen = pg.display.set_mode((500, 500))
        self.screen_rect = self.screen.get_rect()
        self.done = False
        self.keys = pg.key.get_pressed()
        self.clock = pg.time.Clock()
        self.fps = 60.0

    def event_loop(self):
        for event in pg.event.get():
            self.keys = pg.key.get_pressed()
            if event.type == pg.QUIT or self.keys[pg.K_ESCAPE]:
                self.done = True

    def main_loop(self):
        while not self.done:
            self.event_loop()
            self.screen.fill((50, 60, 50))
            pg.display.update()
            self.clock.tick(self.fps)

def main():
    Control().main_loop()
    pg.quit()
    sys.exit()

main()
