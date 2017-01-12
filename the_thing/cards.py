import pygame, time, Functions, draw_text, random

CARD_BACK = pygame.image.load('images/card_back.png')
CARD_FRONT = pygame.image.load('images/card_front2.png')


class Card(pygame.sprite.Sprite):

	deck = []
	card_rooms = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13]
	card_list = [
		["Antidote", "One step closer to\n defeating the monster!"],
		["Antidote", "One step closer to\n defeating the monster!"],
		["Antidote", "One step closer to\n defeating the monster!"],
		["Antidote", "One step closer to\n defeating the monster!"],
		["Joker", "Gotcha!"],
		["Paralyze", "You can't move next\n turn!"],
		["Paralyze", "You can't move next\n turn!"],
		["Radar", "See where the monster\n is!"],
		["Radar", "See where the monster\n is!"],
		["Gas", "The monster can't move\n for 1 turn!"],
		["Gas", "The monster can't move\n for 1 turn!"],
		["2nd Chance", "If the Monster catches\n you, he gets teleported\n to another room!\n\n(Only works once!)"],
		["Teleport", "Move to any room\n on the board...\nOr stay in this one\n if you want to!"],
		["Trampoline", "Get bounced to\n a random room!"],
	]

	def __init__(self, x, y, name=None, description=None):

		pygame.sprite.Sprite.__init__(self)
		self.image = CARD_BACK
		self.name = name
		self.description = description
		self.x = x
		self.y = y
		self.front_image = CARD_FRONT
		Card.deck.append(self)

	def update(self, screen):

		screen.blit(self.image, (self.x, self.y))

	def display_card(self, screen):

		screen.fill((255,250,240))
		screen.blit(CARD_FRONT, (167, 2))
		
		Functions.text_to_screen(screen, self.name, 320, 80, 50, (0, 0, 155))
		desc_text = self.description.splitlines()
		y = 225
		for text in desc_text:
			Functions.text_to_screen(screen, text, 320, y, 25, (0, 0, 100))
			y += 35

	def use_card(self, room_list):
		time.sleep(1.5)
		from game import Game

		if self.name == "Antidote":
			Game.hunter.antidote += 1
		elif self.name == "Paralyze":
			Game.hunter.card_effect = self.name
		elif self.name == "Gas":
			Game.dragon.card_effect = self.name
		elif self.name == "2nd Chance":
			Game.hunter.second_chance = True
		elif self.name == "Trampoline" or self.name == "Teleport":
			Game.room_choice(Game.hunter)
		elif self.name == "Radar":
			Game.dragon.visible = True

		Game.hunter.room.card = None
		Game.pause_for = None


