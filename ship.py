import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
	def __init__(self, ai_settings, screen):
		super().__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		# Loading and get it's rect(rectangle)
		self.image = pygame.image.load('images/ship.bmp').convert()
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()

		# Placing ship in bottom center
		self.rect.x = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom


		# Movement flags
		self.moving_right = False
		self.moving_left = False

	# Borders and speed of moving ship
	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.rect.x += self.ai_settings.ship_speed

		if self.moving_left and self.rect.left > self.screen_rect.left:
			self.rect.x -= self.ai_settings.ship_speed

	def center_ship(self):
		self.rect.x = self.screen_rect.centerx

	# Drawing a ship
	def player(self):
		self.screen.blit(self.image, self.rect)
