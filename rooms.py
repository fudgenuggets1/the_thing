import pygame

SANDY_BROWN = (244,164,96)


class Room():

	room_list = []
	number = 1

	def __init__(self, x, y, w, h, top="wall", bottom="wall", right="wall", left="wall"):
		self.x, self.y = x, y
		self.w, self.h = w, h
		self.top, self.bottom = top, bottom
		self.right, self.left = right, left
		self.number = Room.number
		Room.number += 1
		self.room_list.append(self)

	@staticmethod
	def update(screen):

		for room in Room.room_list:
			pygame.draw.rect(screen, SANDY_BROWN, (room.x, room.y, room.w, room.h), 5)