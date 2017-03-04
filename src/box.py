import os
import pygame

import random

class Box(object):
    def __init__(self, x):
        self.x = x
        self.y = 0
        self.width = 80
        self.height = 80
        s = random.randrange(3)
        if(s == 0):
            string = "bluepresenticon.png"
        elif(s == 1):
            string =  "redpresenticon.png"
        else:
            string = "greenpresenticon.png"
        self.image = pygame.image.load(os.path.join("../res", string)).convert()
        self.image.set_colorkey((0,0,0))
        self.rect = pygame.Rect(x,self.y, self.width, self.height)
        self.fallrate = 2

    def fall(self):
        self.y += self.fallrate

    def fall(self, amount):
        self.y += amount

    def draw(self, screen):
        screen.blit(self.image, [self.x, self.y])
