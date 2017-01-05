import pygame
from rooms import *
from symbols import *
from images import *

def make_map(screen):

	board = []
	for x in range(0, screen.get_width(), 160):
		for y in range(0, screen.get_height(), 120):
			rectangle = Room(x, y, 160, 120)
			board.append(rectangle)
	return board

# Groups and Images

door_png = 'images/door_base.png'
door_image = Image(door_png, 16, 16)
door_symbol = Symbol(door_png, 16, 16, (0, 200, 0))


class Game():

	DOORMOUSE = False

	def __init__(self, screen):

		duhhh = True
		Room.room_list = make_map(screen)

	def update(self, screen):

		mouse_pos = pygame.mouse.get_pos()
		mouse_x = mouse_pos[0]
		mouse_y = mouse_pos[1]
		# Groups and Images
		Room.room_list = make_map(screen)
		door_png = 'images/door_base.png'
		door_image = Image(door_png, mouse_x-16, mouse_y-16)
		door_symbol = Symbol(door_png, 16, 16, (0, 200, 0))

		# DRAWING
		Room.update(screen)

		if door_symbol.clicked or Game.DOORMOUSE:
			
			door_image.update(screen)

		door_symbol.update(screen)