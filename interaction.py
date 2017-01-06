import pygame, sys
from pygame.locals import *
from symbols import Symbol 
from game import Game

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
			if event.key == pygame.K_f:
				toggle_fullscreen()

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
