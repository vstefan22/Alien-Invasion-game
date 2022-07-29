import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
	def __init__(self, ai_settings, screen, ship):
		super().__init__()
		self.screen = screen

		self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
		self.rect.centerx = ship.rect.x + 29
		self.rect.top = ship.rect.y - 13

		self.rect.y = float(self.rect.y)
		self.color = ai_settings.bullet_color
		self.bullet_speed = ai_settings.bullet_speed

	def update(self):
		self.rect.y -= self.bullet_speed

	def draw_bullet(self):
		pygame.draw.rect(self.screen, self.color, self.rect)
