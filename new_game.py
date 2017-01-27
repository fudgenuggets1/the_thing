import pygame, sys, copy, random
from Functions import text_to_screen
from time import sleep
from yo_buttons import Button
from vision import Visible

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
SANDY_BROWN = (244,164,96)

pygame.init()

# Images
door_png = 'images/small_door.png'
door_vertical_png = 'images/small_door_vertical.png'
dragon_png = 'images/dragon4.png'
hunter_png = 'images/hunter1.png'
red_vent_png = 'images/red_vent.png'
BLUE_VENT = pygame.image.load('images/blue_vent.png')
clear_png = 'images/clear.png'
b_png = 'images/b.png'
CARD_BACK = pygame.image.load('images/card_back.png')
CARD_FRONT = pygame.image.load('images/card_front2.png')
h_spawn = pygame.image.load('images/h_spawn.png')
m_spawn = pygame.image.load('images/m_spawn.png')
x_room = pygame.image.load('images/x_room.png')

# Variables
screen = pygame.display.set_mode((800, 625))
screen_height = screen.get_height()
screen_width = screen.get_width()
clock = pygame.time.Clock()
FPS = 20
total_frames = 0
rectangles = []
antidotes_left = 4
antidotes = 0
pause_for = False

gas = False
radar = True
starting_spot = True

def toggle_fullscreen():
	screen = pygame.display.get_surface()
	tmp = screen.convert()
	caption = pygame.display.get_caption()
	cursor = pygame.mouse.get_cursor()  # Duoas 16-04-2007 
	
	w,h = screen.get_width(),screen.get_height()
	flags = screen.get_flags()
	bits = screen.get_bitsize()
	
	pygame.display.quit()
	pygame.display.init()
	
	try:
		screen = pygame.display.set_mode((w,h),flags^FULLSCREEN,bits)
	except:
		screen = pygame.display.set_mode((w,h))
	screen.blit(tmp,(0,0))
	pygame.display.set_caption(*caption)
 
	pygame.key.set_mods(0) #HACK: work-a-round for a SDL bug??
 
	pygame.mouse.set_cursor( *cursor )  # Duoas 16-04-2007
	
	return screen

def interaction(screen):

	mouse_pos = pygame.mouse.get_pos()
	mouse_x = mouse_pos[0]
	mouse_y = mouse_pos[1]
	global Players, Playing

	for event in pygame.event.get():

		if event.type == pygame.QUIT:

			pygame.quit()
			sys.exit()

		if event.type == pygame.KEYDOWN and Playing:
			# Fullscreen mode
			process_key(event)

		if not Players:
			for button in home_screen.Button_List:
				if button.x+button.w > mouse_x > button.x and button.y+button.h > mouse_y > button.y:
					button.mouse_over()
				else:
					button.mouse_off()
			if event.type == pygame.MOUSEBUTTONDOWN:
				for button in home_screen.Button_List:
					if button.mouse_on:
						Players = button.action
		else:
			for button in exit_list:
				if button.x+button.w > mouse_x > button.x and button.y+button.h > mouse_y > button.y:
					button.mouse_over()
				else:
					button.mouse_off()
			if event.type == pygame.MOUSEBUTTONDOWN:
				for button in exit_list:
					if button.mouse_on:
						Players = 0
						Playing = False

def process_key(event):
	
	global pause_for

	if event.key == pygame.K_f:
		toggle_fullscreen()
		
	if not pause_for:	
		if current_turn.piece_type == "Hunter":	
			if event.key == pygame.K_LEFT:
				move_piece(current_turn, 2)
			elif event.key == pygame.K_RIGHT:
				move_piece(current_turn, 3)
			elif event.key == pygame.K_UP:
				move_piece(current_turn, 0)
			elif event.key == pygame.K_DOWN:
				move_piece(current_turn, 1)
		elif current_turn.piece_type == "Monster":
			if event.key == pygame.K_a:
				move_piece(current_turn, 2)
			elif event.key == pygame.K_d:
				move_piece(current_turn, 3)
			elif event.key == pygame.K_w:
				move_piece(current_turn, 0)
			elif event.key == pygame.K_s:
				move_piece(current_turn, 1)
	else:
		if pause_for.room.card:
			pause_for.room.card.use_card(pause_for)


class Piece(pygame.sprite.Sprite):

	monster_number = 2

	def __init__(self, room_number, piece_type, name=None):

		pygame.sprite.Sprite.__init__(self)
		self.piece_type = piece_type
		if self.piece_type == "Monster":
			image = dragon_png
			center_x = 32
			center_y = 32

		elif self.piece_type == "Hunter":
			image = hunter_png
			center_x = 52
			center_y = 32
			self.second_chance = False

		self.image = pygame.image.load(image)
		 # Make our top-left corner the passed-in location.
		self.rect = self.image.get_rect()
		self.rect.x = 0
		self.rect.y = 1
		self.center_x = center_x
		self.center_y = center_y

		self.name = name
		self.room_number = room_number
		self.room = None
		self.visible = True
		self.card_effect = None
		self.new_room_number = None
		self.random_room_number = None
		self.radar_room = False
		self.last_room = self.room_number

	def update_room(self):

		self.room = Room.room_list[self.room_number]

	def update(self, screen):

		self.update_room()
		self.movement()
		if self.visible:
			screen.blit(self.image, (self.rect.x, self.rect.y))
			x = self.name[-1:]
			text_to_screen(screen, x, self.rect.x + self.center_x, self.rect.y - 15, 30, RED)

	def movement(self):
		global pause_for

		
		if self.piece_type == "Monster":	
			
			if radar and not self.new_room_number and not self.random_room_number:	
				self.change_display(False)
				if self.last_room != 12:	
					# FINALLY GOD DAMN
					self.change_display(True)

		if self.new_room_number == None and self.random_room_number == None:	
			self.rect.x = self.room.x + self.center_x
			self.rect.y = self.room.y + self.center_y
		elif self.new_room_number:
			self.move_animation(self.new_room_number)
		elif self.random_room_number:
			self.go_across_board(self.random_room_number)
		if self.room.vent:
			self.use_vent()
		
	def change_display(self, bol):

		if bol:
			self.visible = True
		else:
			self.visible = False

	def move_animation(self, direction):
		global gas, pause_for

		if self.piece_type == "Monster":
			self.change_display(False)
			self.last_room = self.room_number
			if gas:
				self.new_room_number = None
				if current_turn == Monsters[-1]:
					gas = False
				change_turn()

		speed = 10
		if direction == -1:
			self.rect.y -= speed
		
		elif direction == 1:
			self.rect.y += speed

		elif direction == -5:
			self.rect.x -= speed
			
		elif direction == 5:
			self.rect.x += speed

		new_room = Room.room_list[self.room_number + direction]
		if (self.rect.x - self.center_x) == new_room.x and (self.rect.y - self.center_y) == new_room.y:
			self.new_room_number = None
			self.room_number += direction		
			change_turn()
			if self.piece_type == "Hunter" and self.room.card:
				pause_for = self

	def go_across_board(self, new_room_number):

		self.change_display(True)
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
		if (self.rect.x - self.center_x) != new_room.x:
			self.rect.x += change_x
		if (self.rect.y - self.center_y) != new_room.y:
			self.rect.y += change_y
		if (self.rect.x - self.center_x) == new_room.x and (self.rect.y - self.center_y) == new_room.y:
			if self.piece_type == "Monster":
				for hunter in Hunters:	
					if self.room_number == hunter.room_number:
						hunter.second_chance = False
			self.room_number = self.random_room_number
			self.random_room_number = None
			self.update_room()
			
	def use_vent(self):

		if not self.random_room_number and self.room.vent:	
			self.random_room_number = room_choice()

	def change_type(self):
		
		self.piece_type = "Monster"
		self.name = "Monster " + str(Piece.monster_number)
		self.image = pygame.image.load(dragon_png)
		self.center_x = 32
		Hunters.remove(self)
		Monsters.append(self)
		Piece.monster_number += 1


class Card(pygame.sprite.Sprite):

	deck = []
	card_rooms = set([0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 21, 22])
	card_list = [
		["Antidote", "One step closer to\n defeating the monster!"],
		["Antidote", "One step closer to\n defeating the monster!"],
		["Antidote", "One step closer to\n defeating the monster!"],
		["Antidote", "One step closer to\n defeating the monster!"],
		["Paralyze", "You can't move next\n turn!"],
		["Paralyze", "You can't move next\n turn!"],
		["Radar", "See the monster(s)!"],
		["Radar", "See the monster(s)!"],
		["Gas", "The monster(s) can't move\n for 1 turn!"],
		["Gas", "The monster(s) can't move\n for 1 turn!"],
		["2nd Chance", "If the monster catches\n you, he gets teleported\n to another room!\n\n(Only works once!)"],
		["Trampoline", "Get bounced to\n a random room!"],
		["Trampoline", "Get bounced to\n a random room!"],
		["Bouncelator", "Monster(s) get bounced\n to a random room!!"],
		["Bouncelator", "Monster(s) get bounced\n to a random room!!"],
		["Mixer-Upper", "Ever player gets put\n in a random room!"],
		["Joker", "Gotcha!"],
		["Joker", "Gotcha!"],
		["Joker", "Gotcha!"],
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

		screen.blit(CARD_FRONT, (242, 62))
		
		text_to_screen(screen, self.name, 395, 140, 50, (0, 0, 155))
		desc_text = self.description.splitlines()
		y = 295
		for text in desc_text:
			text_to_screen(screen, text, 395, y, 25, (0, 0, 100))
			y += 35

	def use_card(self, piece):
		sleep(1.5)
		global pause_for, antidotes, radar, gas

		if self.name == "Antidote":
			antidotes += 1
		elif self.name == "Paralyze":
			piece.card_effect = self.name
		elif self.name == "Gas":
			gas = True
		elif self.name == "2nd Chance":
			piece.second_chance = True
		elif self.name == "Trampoline":
			piece.random_room_number = room_choice()
			while piece.random_room_number == piece.room_number:
				piece.random_room_number = room_choice()
		elif self.name == "Radar":
			radar = True
		elif self.name == "Bouncelator":
			for monster in Monsters:
				monster.random_room_number = room_choice()
		elif self.name == "Mixer-Upper":
			mixer_upper()
		piece.room.card = None
		pause_for = False

class Room():

	room_list = []
	number = 1

	def __init__(self, x, y, w, h, doors=[1,1,1,1]):
		self.x, self.y = x, y
		self.w, self.h = w, h
		self.doors = doors # UP DOWN LEFT RIGHT
		self.up, self.down = self.doors[0], self.doors[1]
		self.left, self.right = self.doors[2], self.doors[3]
		self.number = Room.number
		self.vent = 0
		self.card = None
		self.radar_room = False
		Room.number += 1
		self.room_list.append(self)

	@staticmethod
	def update(screen):

		for room in Room.room_list:
			
			pygame.draw.rect(screen, SANDY_BROWN, (room.x, room.y, room.w, room.h), 5)

			if room.card:
				room.card.update(screen)

		# Drawing symbols
		screen.blit(BLUE_VENT, (765, 3))
		screen.blit(BLUE_VENT, (3, 565))
		screen.blit(h_spawn, (760, 560))
		screen.blit(h_spawn, (760, 440))
		screen.blit(h_spawn, (600, 560))
		screen.blit(m_spawn, (8, 8))
		screen.blit(x_room, (370, 270))


	@staticmethod
	def make_map():

		cards = copy.deepcopy(Card.card_list)
		random.shuffle(cards)

		board = []
		for x in range(0, 800, 160):
			for y in range(0, 600, 120):
				rectangle = Room(x, y, 160, 120)
				if rectangle.number - 1 in Card.card_rooms:
					new_card = cards.pop()
					rectangle.card = Card(x+68, y+46, new_card[0], new_card[1])
				board.append(rectangle)


		Room.room_list[4].vent = 1
		Room.room_list[20].vent = 1

		Room.room_list[0].doors = [0, 1, 0, 1]
		Room.room_list[1].doors = [1, 1, 0, 1]
		Room.room_list[2].doors = [1, 1, 0, 1]
		Room.room_list[3].doors = [1, 1, 0, 1]
		Room.room_list[4].doors = [1, 0, 0, 1]
		Room.room_list[5].doors = [0, 1, 1, 1]
		Room.room_list[10].doors = [0, 1, 1, 1]
		Room.room_list[15].doors = [0, 1, 1, 1]
		Room.room_list[9].doors = [1, 0, 1, 1]
		Room.room_list[14].doors = [1, 0, 1, 1]
		Room.room_list[19].doors = [1, 0, 1, 1]
		Room.room_list[20].doors = [0, 1, 1, 0]
		Room.room_list[21].doors = [1, 1, 1, 0]
		Room.room_list[22].doors = [1, 1, 1, 0]
		Room.room_list[23].doors = [1, 1, 1, 0]
		Room.room_list[24].doors = [1, 0, 1, 0]

		Room.room_list[12].radar_room = True

		return board


class Home_Screen(Visible):

	def __init__(self):

		Visible.__init__(self)

		buttons = [
			["2 Player", 300, 200, 200, 50, GREEN, BRIGHT_GREEN, 2],
			["3 Player", 300, 300, 200, 50, GREEN, BRIGHT_GREEN, 3],
			["4 Player", 300, 400, 200, 50, GREEN, BRIGHT_GREEN, 4],
		]
		for item in buttons:
			button = Button(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7])
			self.Button_List.append(button)
home_screen = Home_Screen()

def move_piece(piece, direction):
	global starting_spot
	n = piece.room_number
	current_room = Room.room_list[n]
	if piece.card_effect == None: 
		if (not piece.new_room_number and not piece.random_room_number):
			if current_room.doors[direction] == 1:	
				v = piece.room_number
				if direction == 1:
					piece.new_room_number = 1
				elif direction == 0:
					piece.new_room_number = -1
				elif direction == 3:
					piece.new_room_number = 5
				else:
					piece.new_room_number = -5
				if piece == Monster:
					Monster.change_display(False)
					if starting_spot:
						starting_spot = False
	else:
		change_turn()
		piece.card_effect = None

def change_turn():

	global turn_index
	n = pieces.index(current_turn)
	if n < len(pieces) - 1:
		turn_index = n + 1
	else:
		turn_index = 0

def room_choice():
	number = random.randint(0, 24)
	for piece in pieces:
		
		x = piece.room_number

		while True:
			if (x - 1 != number and x + 1 != number) and x != number and (x - 5 != number and x + 5 != number) and (number != 4 and number != 20):	
				break
			number = random.randint(0, 24)
	return number

def check_rooms():

	global radar
	
	radar = False
	for piece in pieces:
		if piece.room.radar_room:
			piece.radar_room = True
			radar = True
		else:
			piece.radar_room = False

	for hunter in Hunters:
		for monster in Monsters:
			if hunter.room_number == monster.room_number:
				if hunter.second_chance and not monster.random_room_number:
					monster.random_room_number = room_choice()
				elif not hunter.second_chance:
					if len(Hunters) < 2:
						end_game(screen, monster)
					else:
						hunter.change_type()
						break

def mixer_upper():
	taken = set([])
	for piece in pieces:
		new_number = room_choice()
		while True:
			if new_number not in taken:
				piece.random_room_number = new_number
				taken.add(new_number)
				break
			else:
				new_number = room_choice()

def get_new_map():

	Room.room_list[:] = []
	Room.number = 1
	Room.room_list = Room.make_map()

def end_game(screen, winner):
	global pause_for, radar
	text_to_screen(screen, "%s wins!" % winner.piece_type, 400, 200, 120, (0, 155, 0))
	radar = True

def display_info(screen):
	# Info
	pygame.draw.rect(screen, (155, 155, 155), (0, 600, 800, 25))
	text_to_screen(screen, "%s's turn" % current_turn.name, 400, 612)
	text_to_screen(screen, "Antidotes left: %s" % antidotes_left, 700, 612)
	# Exit button
	Button.update(screen, exit_list)

def start_new_game(players=2):
	global Monster, Hunter, Hunter2, Hunter3, pieces, Hunters, Monsters, turn_index, current_turn, current_hunter, current_monster, Playing, Players
	Piece.monster_number = 2
	Monster = Piece(0, "Monster", "Monster 1")
	Hunter = Piece(24, "Hunter", "Hunter 1")
	Hunter2 = Piece(19, "Hunter", "Hunter 2")
	Hunter3 = Piece(23, "Hunter", "Hunter 3")
	pieces = []
	Hunters = [Hunter]
	Monsters = [Monster]
	turn_index = 0
	current_turn = 0
	current_hunter = Hunter
	current_monster = Monster
	get_new_map()
	if players == 2:
		pieces = [Hunter, Monster]
	elif players == 3:
		pieces = [Hunter, Hunter2, Monster]
		Hunters.append(Hunter2)
	elif players == 4:
		pieces = [Hunter, Hunter2, Hunter3, Monster]
		Hunters.append(Hunter2)
		Hunters.append(Hunter3)
	Playing = True
	Players = players

Players = None
Playing = False
exit_button = Button("EXIT", 10, 602, 50, 25, RED, BRIGHT_RED, "exit")
exit_list = [exit_button]
while True:

	screen = pygame.display.get_surface()

	screen.fill(FLORAL_WHITE)

	interaction(screen)
	antidotes_left = 4 - antidotes

	if Playing:
		# Logic
		if not pause_for:	
			Room.update(screen)

			for piece in pieces:
				piece.update(screen)

			current_turn = pieces[turn_index]

			if not starting_spot:
				check_rooms()
			
			if current_turn.piece_type == "Hunter":
				current_hunter = current_turn
			else:
				current_monster = current_turn

			for piece in pieces:
				if piece.room.card and piece.piece_type == "Hunter":
					pause_for = piece

		else:
			#for piece in pieces:
			#	if piece.room.card and piece.piece_type == "Hunter":
			pause_for.room.card.display_card(screen)

		# Check if win or lose
		if antidotes == 4:
			for piece in pieces:
				if piece.piece_type == "Hunter":
					end_game(screen, piece)

		display_info(screen)

	else:
		Button.update(screen, home_screen.Button_List)
		if Players == 2:
			start_new_game()
		elif Players == 3:
			start_new_game(3)
		elif Players == 4:
			start_new_game(4)
	pygame.display.set_caption("The Thing     FPS: %s" % int(clock.get_fps()))
	pygame.display.flip()
	clock.tick(FPS)
	total_frames += 1








