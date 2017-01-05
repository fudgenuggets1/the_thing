import pygame, images
from pygame.locals import *


class Symbol(pygame.sprite.Sprite):

	images = pygame.sprite.Group()
	
	def __init__(self, image, x, y, color=None):

		pygame.sprite.Sprite.__init__(self)
		image = images.Image(image, x, y, color)
		self.image = image.image
		 # Make our top-left corner the passed-in location.
		self.rect = self.image.get_rect()
		self.rect.y = x
		self.rect.x = y
		self.color = color
		self.clicked = False
		
		Symbol.images.add(self)

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
			
			if self.color:
				pygame.draw.rect(screen, self.color, (self.rect.x, self.rect.y, 64, 64))
			screen.blit(self.image, (self.rect.x, self.rect.y))


	def mouse_over(self):
		self.mouse_on = True
	def mouse_off(self):
		self.mouse_on = False
	def do_action(self):
		self.clicked = True
		from game import Game
		Game.DOORMOUSE = True





