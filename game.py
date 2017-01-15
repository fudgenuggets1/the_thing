import pygame, Functions, random
from rooms import *
from symbols import *
from images import *
from pieces import *
from cards import *
from yo_buttons import Button

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 200)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
PURPLE = (255, 0, 255)
ORANGE = (255, 155, 0)
BRIGHT_GREEN = (0, 255, 0)
BRIGHT_BLUE = (0, 0, 255)
BRIGHT_RED = (255, 0, 0)
FLORAL_WHITE = (255,250,240)

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
# Card instances
card1 = Card(228, 164)
# 

class Game():

	dragon = The_Thing(dragon_png, 0)
	hunter = Player(hunter_png, 15)
	hunter2 = Player(hunter_png, 15, "Hunter2")
	pieces = [hunter, dragon]
	hunters = [hunter]
	hunter_number = 0
	current_hunter = hunters[hunter_number]
	turn_number = 0
	turn = 0
	pause_for = None
	playing = False
	single_player = Button("1H", 100, 480, 30, 20, GREEN, BRIGHT_GREEN, "single_player")
	two_player = Button("2H", 140, 480, 30, 20, GREEN, BRIGHT_GREEN, "two_player")
	restart_buttons = [single_player, two_player]

	def __init__(self, screen):

		duhhh = True
		Room.room_list = Room.make_map(screen)

	def process(self, screen):

		self.update(screen)

	def home_screen(self, screen):

		single_player = Button("Play: 1 Hunter", 250, 100, 200, 40, GREEN, BRIGHT_GREEN, "single_player")
		two_player = Button("Play: 2 Hunters", 250, 160, 200, 40, GREEN, BRIGHT_GREEN, "two_player")
		Button.update(screen, Button.List)

	def update(self, screen):

		mouse_pos = pygame.mouse.get_pos()
		mouse_x = mouse_pos[0]
		mouse_y = mouse_pos[1]
		
		# DRAWING
		Room.update(screen)

		for piece in Game.pieces:
			piece.update(screen)

		Game.turn = Game.pieces[Game.turn_number]
		Game.current_hunter = Game.hunters[Game.hunter_number]

		# Logic
		self.game_logic(screen)

	def game_logic(self, screen):

		if Game.hunter.room.card:
			Game.pause_for = Game.hunter
			Game.hunter.room.card.display_card(screen)
		else:
			antidotes = 4 - Game.hunter.antidote
			text_list = [
				["Restart:", 40, 492],
				["%s's turn" % Game.turn.name, 320, 492],
				["Antidotes left: %s" % antidotes, 550, 492],
			]
			for text in text_list:
				Functions.text_to_screen(screen, text[0], text[1], text[2], 20, BLACK)
			Button.update(screen, Game.restart_buttons)


		if Game.dragon.room_number == Game.hunter.room_number:
			if not Game.hunter.second_chance:
				Game.end_game(screen, Game.dragon)
			elif Game.hunter.second_chance and not Game.dragon.moving_far:
				Game.room_choice(Game.dragon)
		if Game.hunter.antidote == 4:
			Game.end_game(screen, Game.hunter)

		for piece in Game.pieces:
			if piece.room.radar_room:
				Game.dragon.visible = True

	@staticmethod
	def change_turn(last_moved):

		for piece in Game.pieces:
			if piece != last_moved:
				pass
			else:
				piece.card_effect = None
		n = Game.pieces.index(last_moved)
		if n < len(Game.pieces) - 1:
			Game.turn_number = n + 1
		else:
			Game.turn_number = 0

		Game.dragon.visible = False

	@staticmethod
	def end_game(screen, winner):

		Functions.text_to_screen(screen, "%s wins!" % winner.name, 320, 240, 100, (0, 155, 0))
		Game.pause_for = True
		Game.dragon.visible = True

	@staticmethod
	def room_choice(piece):

		number = random.randint(0, 15)
		while number == Game.dragon.room_number or number == Game.hunter.room_number:
			number = random.randint(0, 15)
		piece.moving_far = number

	@staticmethod
	def restart():

		Game.dragon = The_Thing(dragon_png, 0)
		Game.hunter = Player(hunter_png, 15)
		Game.hunter2 = Player(hunter_png, 15, "Hunter2")
		Game.pieces = [Game.hunter, Game.dragon]
		Game.hunters = [Game.hunter]
		Game.turn_number = 0
		Game.turn = 0
		Game.pause_for = None






