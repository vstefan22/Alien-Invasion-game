import pygame
import pygame.font


class SettingsButton:
	def __init__(self, ai_settings, screen):
		self.screen = screen
		self.ai_settings = ai_settings
		self.screen_rect = self.screen.get_rect()

		self.width, self.height = 200, 50
		self.color = (0, 255, 0)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.Font('invasion.TTF', 40)

		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.x = self.screen_rect.left + 20
		self.rect.y = self.screen_rect.centery
		self.prep_settings()

	def prep_settings(self):
		self.image = self.font.render("Settings", True, self.text_color, None)
		self.image_rect = self.image.get_rect()
		self.image_rect.x = self.rect.x + 12
		self.image_rect.y = self.rect.centery - 17


	def show_settings(self):
		self.screen.blit(self.image, (self.image_rect.x, self.image_rect.y))