import pygame
import pygame.font


class ExitButton:
	def __init__(self, ai_settings, screen):
		self.screen = screen
		self.ai_settings = ai_settings
		self.screen_rect = self.screen.get_rect()

		self.width, self.height = 200, 50
		self.text_color = (255, 255, 255)
		self.font = pygame.font.Font('invasion.TTF', 40)

		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.x = self.screen_rect.left + 20
		self.rect.bottom = self.screen_rect.centery + 300
		self.prep_exit()

	def prep_exit(self):
		self.image = self.font.render("Exit", True, self.text_color, None)
		self.image_rect = self.image.get_rect()
		self.image_rect.x = self.rect.x + 20
		self.image_rect.y = self.rect.bottom - 20


	def show_exit(self):
		self.screen.blit(self.image, (self.image_rect.x, self.image_rect.y))