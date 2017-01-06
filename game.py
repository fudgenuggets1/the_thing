import pygame
from rooms import *
from symbols import *
from images import *

def make_map(screen):

	board = []
	for x in range(0, 640, 160):
		for y in range(0, 480, 120):
			rectangle = Room(x, y, 160, 120)
			board.append(rectangle)
	return board


symbol_x = 648
# Groups, Images, and Symbols
door_png = 'images/small_door.png'
door_vertical_png = 'images/small_door_vertical.png'
dragon_png = 'images/dragon4.png'
red_vent_png = 'images/red_vent.png'
blue_vent_png = 'images/blue_vent.png'
clear_png = 'images/clear.png'
b_png = 'images/b.png'
door_image = Image(door_png, 16, 16)
thing_image = Image(dragon_png, 24, 64)
b_image = Image(b_png, 552, 392)
clear_symbol = Symbol(clear_png, symbol_x, 8, action="clear")
door_symbol = Symbol(door_png, symbol_x, 96, (0, 200, 0))
door_vertical_symbol = Symbol(door_vertical_png, symbol_x, 136, (0, 200, 0), "door_vertical")
red_vent_symbol = Symbol(red_vent_png, symbol_x, 200, (200, 0, 0), "red_vent")
blue_vent_symbol = Symbol(blue_vent_png, symbol_x, 240, (200, 0, 0), "blue_vent")



class Game():

	MOUSE = False
	images = [thing_image, b_image]
	symbols = [
		clear_symbol,
		door_symbol,
		door_vertical_symbol,
		red_vent_symbol,
		blue_vent_symbol,
	]

	def __init__(self, screen):

		duhhh = True
		Room.room_list = make_map(screen)

	def update(self, screen):

		mouse_pos = pygame.mouse.get_pos()
		mouse_x = mouse_pos[0]
		mouse_y = mouse_pos[1]
		
		# DRAWING
		Room.update(screen)

		if Game.MOUSE:
			
			Game.MOUSE.update(screen)

		Game.update_symbols(screen)

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






