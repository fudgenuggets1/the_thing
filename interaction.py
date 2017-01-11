import pygame, sys
from pygame.locals import *
from symbols import Symbol 
from game import Game
from rooms import Room

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

	for event in pygame.event.get():

		if event.type == pygame.QUIT:

			pygame.quit()
			sys.exit()

		if event.type == pygame.KEYDOWN:
			# Fullscreen mode
			if event.key == pygame.K_f:
				toggle_fullscreen()
			if Game.pause_for == None:	
				# Player movement
				if Game.turn == Game.hunter:
					if event.key == pygame.K_UP:
						Room.move_piece(Game.hunter, 0)
					elif event.key == pygame.K_DOWN:
						Room.move_piece(Game.hunter, 1)
					elif event.key == pygame.K_RIGHT:
						Room.move_piece(Game.hunter, 3)
					elif event.key == pygame.K_LEFT:
						Room.move_piece(Game.hunter, 2)
				# The Thing movement
				elif Game.turn == Game.dragon:
					if event.key == pygame.K_w:
						Room.move_piece(Game.dragon, 0)
					elif event.key == pygame.K_s:
						Room.move_piece(Game.dragon, 1)
					elif event.key == pygame.K_d:
						Room.move_piece(Game.dragon, 3)
					elif event.key == pygame.K_a:
						Room.move_piece(Game.dragon, 2)

					elif event.key == pygame.K_v:
						Room.move_piece(Game.dragon, 4)
			else:
				Game.hunter.room.card.use_card(Room.room_list)

		for button in Symbol.images:
			if button.rect.x+button.rect.w > mouse_x > button.rect.x and button.rect.y+button.rect.h > mouse_y > button.rect.y:
				button.mouse_over()
			else:
				button.mouse_off()

		if event.type == pygame.MOUSEBUTTONDOWN:
			for button in Symbol.images:
				if button.mouse_on:
					button.do_action()
					break
				if Game.MOUSE:
					Game.place_symbol()
