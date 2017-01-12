from pygame import *

# draw some text into an area of a surface
# automatically wraps words
# returns any text that didn't get blitted
def drawText(surface, text, rect, color=(128, 128, 128), font_type='Arial', aa=False, bkg=None):
	
	rect = Rect(rect)
	y = rect.top
	lineSpacing = -2
 
	# get the height of the font
	Height = font.SysFont(font_type, 25)
	fontHeight = Height.size(text)[0]
 
	while text:
		i = 1
 
		# determine if the row of text will be outside our area
		if y + fontHeight > rect.bottom:
			break
 
		# determine maximum width of line
		while font.size(text[:i])[0] < rect.width and i < len(text):
			i += 1
 
		# if we've wrapped the text, then adjust the wrap to the last word      
		if i < len(text): 
			i = text.rfind(" ", 0, i) + 1
 
		# render the line and blit it to the surface
		if bkg:
			image = font.render(text[:i], 1, color, bkg)
			image.set_colorkey(bkg)
		else:
			image = font.render(text[:i], aa, color)
 
		surface.blit(image, (rect.left, y))
		y += fontHeight + lineSpacing
 
		# remove the text we just blitted
		text = text[i:]
 
	return text