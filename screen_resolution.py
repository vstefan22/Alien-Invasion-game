import pygame
import pygame.font
import game_functions as gf


class Resolution:
	def __init__(self, ai_settings, screen):
		self.ai_settings = ai_settings
		self.screen = screen
		self.screen_rect = self.screen.get_rect()

		self.color = (255, 255, 255)
		self.bg_color = (148, 148, 148)
		self.bg_color_ = (108, 108, 108)
		self.font = pygame.font.Font("invasion.TTF", 20)

		self.width, self.height = 230, 30
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.x = self.screen_rect.left + 60
		self.rect.y = self.screen_rect.top + 190
		self.width_ = 130
		self.height_ = 30
		self.rect_resolution = pygame.Rect(0, 0, self.width_, self.height_)
		self.rect_resolution.x = self.screen_rect.left + 70
		self.rect_resolution.y = self.screen_rect.top + 230

		self.prep_resolution()
		self.prep_resolution_menu()

	def prep_resolution(self):
		self.image = self.font.render("-Screen resolution:", True, self.color, self.bg_color)
		self.image_rect = self.image.get_rect()
		self.image_x = self.rect.left
		self.image_y = self.rect.y

	def prep_resolution_menu(self):
		self.image_ = self.font.render("1280x800", True, self.color, self.bg_color_)
		self.image_rect_ = self.image.get_rect()
		self.image_x_ = self.rect_resolution.x + 10
		self.image_y_ = self.rect_resolution.y

	def blit_resolution(self):
		self.screen.fill(self.bg_color, self.rect)
		self.screen.blit(self.image, (self.image_x, self.image_y))

	def blit_resolution_menu(self):
		self.screen.fill(self.bg_color_, self.rect_resolution)
		self.screen.blit(self.image_, (self.image_x_, self.image_y_))
