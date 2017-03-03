import os
import pygame

class Grinch(object):
    def __init__(self, screenx, screeny):
	self.height = 79 #size of current file, should be changed if we change files
	self.width = 75 #see above
        self.x = (screenx - self.width)/2
	self.y = screeny - self.height
	self.image = pygame.image.load(os.path.join("res", "grinchicon.png")).convert()
	self.image.set_colorkey((0,0,255))
	self.rect = pygame.Rect(self.x,self.y, self.width, self.height)

    def draw(self, screen):
        screen.blit(self.image, [self.x, self.y])
