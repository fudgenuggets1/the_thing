import pygame, random

SANDY_BROWN = (244,164,96)
SMALL_DOOR = pygame.image.load('images/small_door.png')
SMALL_DOOR_VERTICAL = pygame.image.load('images/small_door_vertical.png')
RED_VENT = pygame.image.load('images/red_vent.png')
BLUE_VENT = pygame.image.load('images/blue_vent.png')



class Room():

	room_list = []
	number = 1

	def __init__(self, x, y, w, h, doors=[0,0,0,0]):
		self.x, self.y = x, y
		self.w, self.h = w, h
		self.doors = doors # UP DOWN LEFT RIGHT
		self.up, self.down = self.doors[0], self.doors[1]
		self.left, self.right = self.doors[2], self.doors[3]
		self.number = Room.number
		self.vent = 0
		self.card = None
		Room.number += 1
		self.room_list.append(self)

	@staticmethod
	def update(screen):

		for room in Room.room_list:

			if room.doors[0] == 1:
				screen.blit(SMALL_DOOR_VERTICAL, (room.x+66, room.y-16))
			
			pygame.draw.rect(screen, SANDY_BROWN, (room.x, room.y, room.w, room.h), 5)
			
			if room.doors[3] == 1:
				screen.blit(SMALL_DOOR, (room.x+144, room.y+44))

			if room.card:
				room.card.update(screen)

		screen.blit(BLUE_VENT, (605, 3))
		screen.blit(BLUE_VENT, (3, 445))
		screen.blit(RED_VENT, (285, 243))
		screen.blit(RED_VENT, (323, 205))


	@staticmethod
	def make_map(screen):
		from cards import Card
		card_list = Card.card_list
		random.shuffle(card_list)

		board = []
		for x in range(0, 640, 160):
			for y in range(0, 480, 120):
				rectangle = Room(x, y, 160, 120)
				try:	
					card_info = card_list.pop()
					rectangle.card = Card(x+68, y+46, card_info[0], card_info[1])
				except:
					rectangle.card = Card(x+68, y+46)
				board.append(rectangle)
		
		Room.room_list[0].doors = [0, 1, 0, 1]
		Room.room_list[1].doors = [1, 1, 0, 1]
		Room.room_list[2].doors = [1, 1, 0, 1]
		Room.room_list[3].doors = [1, 0, 0, 1]
		Room.room_list[4].doors = [0, 0, 1, 1]
		Room.room_list[5].doors = [0, 0, 1, 1]
		Room.room_list[6].doors = [0, 1, 1, 1]
		Room.room_list[7].doors = [1, 0, 1, 1]
		Room.room_list[8].doors = [0, 1, 1, 1]
		Room.room_list[9].doors = [1, 0, 1, 1]
		Room.room_list[10].doors = [0, 0, 1, 1]
		Room.room_list[11].doors = [0, 0, 1, 1]
		Room.room_list[12].doors = [0, 1, 1, 0]
		Room.room_list[13].doors = [1, 1, 1, 0]
		Room.room_list[14].doors = [1, 1, 1, 0]
		Room.room_list[15].doors = [1, 0, 1, 0]

		Room.room_list[3].vent = 1
		Room.room_list[12].vent = 1
		Room.room_list[6].vent = 2
		Room.room_list[9].vent = 2

		Room.room_list[11].card = None
		Room.room_list[14].card = None
		Room.room_list[15].card = None




		return board

	@staticmethod
	def move_piece(piece, direction):
		from game import Game
		n = piece.room_number
		current_room = Room.room_list[n]
		if piece.card_effect == None:
			try:	
				if current_room.doors[direction] == 1:
					if direction == 1:
						piece.moving += 1
					elif direction == 0:
						piece.moving -= 1
					elif direction == 3:
						piece.moving += 4
					else:
						piece.moving -= 4

			except:
				if direction == 4:
					if current_room.vent > 0:	
						vent_number = current_room.vent
						for room in Room.room_list:
							if room.vent == vent_number and room != current_room:
								new_number = Room.room_list.index(room)
								piece.room_number = new_number
								Game.change_turn(piece)
								break

			if piece == Game.dragon:
				Game.dragon.visible = False
		else:
			Game.change_turn(piece)

	








