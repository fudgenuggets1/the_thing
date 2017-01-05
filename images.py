import pygame


class Image(pygame.sprite.Sprite):

	all_images = pygame.sprite.Group()

	def __init__(self, image, x, y, color=None):

		self.image = image
		self.x, self.y = x, y
		self.color = color

	def update(self, screen):
		
		pass




class Text_Image(Image):

	all_images = pygame.sprite.Group()

	def __init__(self, text, x, y, color=None):
		Image.__init__(self, image="")

	



	