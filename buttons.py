import pygame as pyg
#button class
class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pyg.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False
		self.mouse_out = pyg.mouse.get_pressed()[0]
		


	def draw(self, surface):

		action = False
		#blit himself on the screen
		surface.blit(self.image, (self.rect.x, self.rect.y))
		
		#how to get the mouse position
		pos = pyg.mouse.get_pos()
		
		#mouse pointing the rect the "button" and waiting for a clicked
		if self.rect.collidepoint(pos):
			if pyg.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True
			if pyg.mouse.get_pressed()[0] == 0:
				self.clicked = False

		return action














































