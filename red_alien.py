import pygame
from pygame.sprite import Sprite


class RedAlien(Sprite):
	def __init__(self, screen, ai_settings):
		super().__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		self.image = pygame.image.load("Images/red ship.png")
		self.rect = self.image.get_rect()
		self.rect.x = self.image.get_width()
		self.rect.y = self.image.get_height()
		self.x = float(self.rect.x)

	def red_alien(self):
		self.screen.blit(self.image, self.rect)

	def check_edges(self):
		self.screen_rect = self.screen.get_rect()
		if self.rect.right >= self.screen_rect.right:
			return True
		elif self.rect.left < 0:
			return True

	def update(self):
		self.x += (self.ai_settings.red_alien_speed * self.ai_settings.fleet_direction)
		self.rect.x = self.x
