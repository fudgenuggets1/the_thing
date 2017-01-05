import pygame


class Image(pygame.sprite.Sprite):

	all_images = pygame.sprite.Group()

	def __init__(self, image, x, y, color=None):

		self.image = pygame.image.load(image)
		self.x, self.y = x, y
		self.color = color
		#Image.all_images.add(self)

	def update(self, screen):
		
		mouse_pos = pygame.mouse.get_pos()
		mouse_x = mouse_pos[0]
		mouse_y = mouse_pos[1]
		self.x, self.y = mouse_x, mouse_y
		screen.blit(self.image, (self.x-32, self.y-32))




class Text_Image(Image):

	all_images = pygame.sprite.Group()

	def __init__(self, text, x, y, color=None):
		Image.__init__(self, image="")

	



	