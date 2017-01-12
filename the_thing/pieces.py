import pygame
from rooms import *


class Piece(pygame.sprite.Sprite):

	def __init__(self, image, room_number):

		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(image)
		 # Make our top-left corner the passed-in location.
		self.rect = self.image.get_rect()
		self.rect.x = 1
		self.rect.y = 2
		self.center_x = 0
		self.center_y = 0

		self.room_number = room_number
		self.room = None
		self.visible = True
		self.card_effect = None
		self.moving = 0
		self.moving_far = 0

	def move_animation(self, direction):
		from game import Game

		speed = 10
		if direction == -1:
			self.rect.y -= speed
		
		elif direction == 1:
			self.rect.y += speed

		elif direction == -4:
			self.rect.x -= speed
			
		elif direction == 4:
			self.rect.x += speed

		new_room = Room.room_list[self.room_number + direction]
		if (self.rect.x - self.center_x) == new_room.x and (self.rect.y - self.center_y) == new_room.y:
			self.moving = 0
			self.room_number += direction
			Game.change_turn(self)

	def go_across_board(self, new_room_number):
		from game import Game

		self.visible = True

		change_x = 0
		change_y = 0
		speed = 5

		current_room = self.room
		new_room = Room.room_list[new_room_number]
		if current_room.x > new_room.x:
			change_x = -5
		elif current_room.x < new_room.x:
			change_x = 5
		if current_room.y > new_room.y:
			change_y = -5
		elif current_room.y < new_room.y:
			change_y = 5
		if (self.rect.x - self.center_x) == new_room.x and (self.rect.y - self.center_y) == new_room.y:
			self.moving_far = 0
			self.room_number = new_room_number
			if self.name == "Monster":
				Game.hunter.second_chance = False
		if (self.rect.x - self.center_x) != new_room.x:
			self.rect.x += change_x
		if (self.rect.y - self.center_y) != new_room.y:
			self.rect.y += change_y


class The_Thing(Piece):

	def __init__(self, image, room_number):
		Piece.__init__(self, image, room_number)
		self.name = "Monster"
		self.center_x = 24
		self.center_y = 24

	def update(self, screen):
		from rooms import Room
		
		self.room = Room.room_list[self.room_number]
		if not self.moving and not self.moving_far:	
			self.rect.x = self.room.x + self.center_x
			self.rect.y = self.room.y + self.center_y
		elif self.moving:
			self.move_animation(self.moving)
		elif self.moving_far:
			self.go_across_board(self.moving_far)
		if self.visible:
			screen.blit(self.image, (self.rect.x, self.rect.y))


class Player(Piece):

	number = 1
	antidote = 0

	def __init__(self, image, room_number):
		Piece.__init__(self, image, room_number)
		self.name = "Hunter"
		self.center_x = 52
		self.center_y = 32
		self.antidote = Player.antidote
		self.second_chance = False
		Player.number += 1

	def update(self, screen):
		from rooms import Room
		self.room = Room.room_list[self.room_number]
		if not self.moving and not self.moving_far:	
			self.rect.x = self.room.x + self.center_x
			self.rect.y = self.room.y + self.center_y
		elif self.moving:
			self.move_animation(self.moving)
		elif self.moving_far:
			self.go_across_board(self.moving_far)
		self.see_card = False
		screen.blit(self.image, (self.rect.x, self.rect.y))



