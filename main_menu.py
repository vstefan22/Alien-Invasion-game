import pygame
import pygame.font

class MainMenu():
	def __init__(self, screen, ai_settings):
		self.screen = screen
		self.ai_settings = ai_settings
		self.screen_width()

	def screen_width(self):
		if self.ai_settings.screen_width == 1280:
			self.image = pygame.image.load('Images/galaxy (3).jpg')
			self.rect = self.image.get_rect()

		if self.ai_settings.screen_width == 1920:
			self.image = pygame.image.load("Images/galaxy (1).jpg")
			self.rect = self.image.get_rect()
		self.rect.centerx = self.rect.centerx
		self.rect.centery = self.rect.centery
		self.color = (255, 255, 255)
		self.bg_color = self.ai_settings.settings_color
		self.font = pygame.font.Font('invasion.TTF', 48)
		self.prep_space_invaders()

	def prep_space_invaders(self):
		self.image_ = self.font.render("SPACE INVADERS", True, self.color, None)

		self.image_x = 420
		self.image_y = self.rect.y + 30

	def show(self):
		self.screen.blit(self.image, self.rect)
		self.screen.blit(self.image_, (self.image_x, self.image_y))

