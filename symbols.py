import pygame, images
from pygame.locals import *


class Symbol(pygame.sprite.Sprite):

	images = pygame.sprite.Group()
	
	def __init__(self, image, x, y, color=None, action="door"):

		pygame.sprite.Sprite.__init__(self)
		image = images.Image(image, x, y, color)
		self.image = image
		 # Make our top-left corner the passed-in location.
		self.rect = self.image.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.color = color
		self.clicked = False
		self.action = action
		
		Symbol.images.add(self)

	def update(self, screen):
			
		if self.color:
			pygame.draw.rect(screen, self.color, (self.rect.x, self.rect.y, self.image.image.get_width(), self.image.image.get_height()))
		screen.blit(self.image.image, (self.rect.x, self.rect.y))


	def mouse_over(self):
		self.mouse_on = True
	def mouse_off(self):
		self.mouse_on = False
	def do_action(self):
		
		from game import Game
		
		pass



