import pygame
from pygame.locals import *


class symbol(pygame.sprite.Sprite):

	images = pygame.sprite.Group()
	
	def __init__(self):

		pygame.sprite.Sprite.__init__(self)
		self.image = jill_image.image.convert()
		 # Make our top-left corner the passed-in location.
		self.rect = self.image.get_rect()
		self.rect.y = 472
		self.rect.x = 50

	def update(self, screen):

		try:	
			self.angle += self.turn_speed
			if self.angle >= 360:
				self.angle = 0
			self.image = 0
			self.image = pygame.transform.rotate(jack_image.image, self.angle)
			self.center = self.rect.center
			self.rect.x += Jack.change_x
			self.rect.y += Jack.change_y
		except:
			screen.blit(self.image, (self.rect.x, self.rect.y))
			print(self.image + self.rect.x + self.rect.y)

	def effect(ev):

		pass