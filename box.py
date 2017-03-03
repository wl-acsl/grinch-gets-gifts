import pygame

class Box(object):
    def __init__(self, x, y, width, height):
        self.x = x
	self.y = y
	self.width = width
	self.height = height
	self.image = pygame.image.load("bluepresenticon.png").convert()
	self.rect = pygame.Rect(x,y, width, height)
