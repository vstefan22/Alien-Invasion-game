import pygame
from pygame.sprite import Sprite


class AlienBullet(Sprite):
	def __init__(self, ai_settings, screen, red_aliens):
		super().__init__()
		self.screen = screen

		self.rect = pygame.Rect(0, 0, ai_settings.alien_bullet_width, ai_settings.alien_bullet_height)

		self.rect.centerx = red_aliens.rect.centerx
		self.rect.top = red_aliens.rect.bottom

		self.rect.y = float(self.rect.y)
		self.color = ai_settings.alien_bullet_color
		self.bullet_speed = ai_settings.alien_bullet_speed

	def update(self):
		self.rect.y += self.bullet_speed

	def draw_alien_bullet(self):
		pygame.draw.rect(self.screen, self.color, self.rect)
