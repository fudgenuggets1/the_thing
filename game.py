import pygame, Functions, random
from rooms import *
from symbols import *
from images import *
from pieces import *
from cards import *

symbol_x = 648
# Images
door_png = 'images/small_door.png'
door_vertical_png = 'images/small_door_vertical.png'
dragon_png = 'images/dragon4.png'
hunter_png = 'images/hunter1.png'
red_vent_png = 'images/red_vent.png'
blue_vent_png = 'images/blue_vent.png'
clear_png = 'images/clear.png'
b_png = 'images/b.png'
# Image instances
door_image = Image(door_png, 16, 16)
thing_image = Image(dragon_png, 24, 64)
b_image = Image(b_png, 552, 392)
# Symbol instances
clear_symbol = Symbol(clear_png, symbol_x, 8, action="clear")
door_symbol = Symbol(door_png, symbol_x, 96, (0, 200, 0))
door_vertical_symbol = Symbol(door_vertical_png, symbol_x, 136, (0, 200, 0), "door_vertical")
red_vent_symbol = Symbol(red_vent_png, symbol_x, 200, (200, 0, 0), "red_vent")
blue_vent_symbol = Symbol(blue_vent_png, symbol_x, 240, (200, 0, 0), "blue_vent")
# Card instances
card1 = Card(228, 164)


class Game():

	MOUSE = False
	images = []
	symbols = [
		clear_symbol,
		door_symbol,
		door_vertical_symbol,
		red_vent_symbol,
		blue_vent_symbol,
	]
	dragon = The_Thing(dragon_png, 0)
	hunter = Player(hunter_png, 15)
	pieces = [hunter, dragon]
	turn_number = 0
	turn = 0
	pause_for = None

	def __init__(self, screen):

		duhhh = True
		Room.room_list = Room.make_map(screen)

	def update(self, screen):

		mouse_pos = pygame.mouse.get_pos()
		mouse_x = mouse_pos[0]
		mouse_y = mouse_pos[1]
		
		# DRAWING
		Room.update(screen)

		if Game.MOUSE:
			
			Game.MOUSE.update(screen)

		Game.update_symbols(screen)
		for piece in Game.pieces:
			piece.update(screen)

		Game.turn = Game.pieces[Game.turn_number]

		if Game.hunter.room.card:
			Game.pause_for = Game.hunter
			Game.hunter.room.card.display_card(screen)
		else:
			Functions.text_to_screen(screen, "%s's turn" % Game.turn.name, 300, 492, 20, (0,0,0))
			antidotes = 4 - Game.hunter.antidote
			Functions.text_to_screen(screen, "Antidotes left: %s" % antidotes, 500, 492, 20, (0,0,0))

		if Game.dragon.room_number == Game.hunter.room_number:
			if not Game.hunter.second_chance:
				Game.end_game(screen, Game.dragon)
			elif Game.hunter.second_chance and not Game.dragon.moving_far:
				Game.room_choice(Game.dragon)
		if Game.hunter.antidote == 4:
			Game.end_game(screen, Game.hunter)

	@staticmethod
	def place_symbol():

		if Game.MOUSE:

			new_image = Game.MOUSE
			Game.images.append(new_image)
			Game.MOUSE = None

	@staticmethod
	def update_symbols(screen):

		for img in Game.images:
			screen.blit(img.image, (img.x-16, img.y-16))

		for symbol in Game.symbols:	
			symbol.update(screen)

	@staticmethod
	def clear_board():

		Game.images[:] = []
		Game.images = [thing_image, b_image]

	@staticmethod
	def change_turn(last_moved):

		for piece in Game.pieces:

			if piece != last_moved:
				Game.turn_number = Game.pieces.index(piece)
			else:
				piece.card_effect = None
		
	@staticmethod
	def end_game(screen, winner):

		Functions.text_to_screen(screen, "%s wins!" % winner.name, 320, 240, 100, (0, 155, 0))
		Game.pause_for = True
		Game.dragon.visible = True

	@staticmethod
	def room_choice(piece):

		number = random.randint(0, 15)
		while number == Game.dragon.room_number and number != Game.hunter.room_number:
			number = random.randint(0, 15)
		piece.moving_far = number



