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


class Game():

	def __init__(self, screen):

		duhhh = True

	def update(self, screen):

		# Groups and Images
		Room.room_list = make_map(screen)

		# DRAWING
		Room.update(screen)