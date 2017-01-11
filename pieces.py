import pygame


class Piece(pygame.sprite.Sprite):

	def __init__(self, image, room_number):

		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(image)
		 # Make our top-left corner the passed-in location.
		self.rect = self.image.get_rect()
		self.rect.x = 1
		self.rect.y = 2

		self.room_number = room_number
		self.room = None
		self.visible = True
		self.card_effect = None


class The_Thing(Piece):

	def __init__(self, image, room_number):
		Piece.__init__(self, image, room_number)
		self.name = "Monster"

	def update(self, screen):
		from rooms import Room
		self.room = Room.room_list[self.room_number-1]
		self.rect.x = self.room.x + 24
		self.rect.y = self.room.y + 24
		if self.visible:
			screen.blit(self.image, (self.rect.x, self.rect.y))


class Player(Piece):

	number = 1
	antidote = 0

	def __init__(self, image, room_number):
		Piece.__init__(self, image, room_number)
		self.name = "Hunter"
		self.antidote = Player.antidote
		self.second_chance = False
		Player.number += 1

	def update(self, screen):
		from rooms import Room
		self.room = Room.room_list[self.room_number-1]
		self.rect.x = self.room.x + 52
		self.rect.y = self.room.y + 32
		self.see_card = False
		screen.blit(self.image, (self.rect.x, self.rect.y))



