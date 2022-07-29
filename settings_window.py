import pygame
import pygame.font


class SettingsTab:
	def __init__(self, screen, ai_settings):
		self.screen = screen
		self.ai_settings = ai_settings
		self.screen_rect = self.screen.get_rect()
		if self.ai_settings.screen_width == 1920:
			self.image = pygame.image.load("Images/settings_background.jpg")
		if self.ai_settings.screen_width == 1280:
			self.image = pygame.image.load("Images/galaxy (3).jpg")
		self.rect = self.image.get_rect()
		self.space_ship = pygame.image.load("Images/ship.png")
		self.image_x_ = 890
		self.image_y_ = 80
		self.color = (255, 255, 255)
		self.bg_color = self.ai_settings.settings_color
		self.font = pygame.font.Font('invasion.TTF', 48)
		self.screen_font = pygame.font.Font('invasion.TTF', 30)
		self.prep_settings()
		self.prep_screen_settings()
		self.prep_sound_settings()
		self.rect.x = 640
		self.rect.y = self.screen_rect.top

	def prep_settings(self):
		self.image = self.font.render("Settings", True, self.color, self.bg_color)
		self.image_rect = self.image.get_rect()
		self.image_x = 520
		self.image_y = self.rect.y + 30

	def prep_screen_settings(self):
		self.screen_image = self.screen_font.render("Screen settings:", True, self.color, self.bg_color)
		self.screen_image_rect = self.image.get_rect()
		self.screen_image_x = self.rect.left + 30
		self.screen_image_y = self.rect.y + 150

	def prep_sound_settings(self):
		self.sound_image = self.screen_font.render("Controls & shortcuts:", True, self.color, self.bg_color)
		self.sound_image_rect = self.image.get_rect()
		self.sound_image_x = self.rect.left + 30
		self.sound_image_y = self.rect.y + 300

	def show_settings(self):
		self.screen.blit(self.sound_image, (self.sound_image_x, self.sound_image_y))
		self.screen.blit(self.screen_image, (self.screen_image_x, self.screen_image_y))
		self.screen.blit(self.image, (self.image_x, self.image_y))
		self.screen.blit(self.space_ship, (self.image_x_, self.image_y_))
