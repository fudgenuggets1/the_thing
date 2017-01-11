import pygame, textwrap

def text_to_screen(screen, text, x, y, size = 25,
	color = (255,255,255), font_type = 'Arial'):

	text = str(text)

	font = pygame.font.SysFont(font_type, size)
	size = font.size(text)
	text = font.render(text, True, color)

	screen.blit(text, (x-(size[0]/2), y-(size[1]/2)))

	
		
