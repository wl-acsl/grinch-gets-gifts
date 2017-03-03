import os
import pygame

class Box(object):
    def __init__(self, x):
        self.x = x
	self.y = 0
	self.width = 80
	self.height = 80
	self.image = pygame.image.load(os.path.join("../res", "bluepresenticon.png")).convert()
	self.rect = pygame.Rect(x,self.y, self.width, self.height)
        self.fallrate = 2

    def fall(self):
        self.y += self.fallrate

    def fall(self, amount):
	self.y += amount

    def draw(self, screen):
        screen.blit(self.image, [self.x, self.y])
