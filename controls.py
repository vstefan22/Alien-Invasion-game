import pygame
import pygame.font


class Controls:
	def __init__(self, ai_settings, screen):
		self.ai_settings = ai_settings
		self.screen = screen
		self.screen_rect = self.screen.get_rect()

		self.color = (255, 255, 255)
		self.bg_color = (128, 128, 128)
		self.bg_color_ = (108, 108, 108)
		self.font = pygame.font.Font("invasion.TTF", 20)

		self.width, self.height = 135, 30
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.x = self.screen_rect.left + 60
		self.rect.y = self.screen_rect.top + 350

		self.rect_1 = pygame.Rect(0, 0, self.width + 20, self.height)
		self.rect_1.y = self.rect.y + 60
		self.rect_1.x = self.screen_rect.left + 60

		self.rect_2 = pygame.Rect(0, 0, self.width + 20, self.height)
		self.rect_2.y = self.rect.y + 120
		self.rect_2.x = self.screen_rect.left + 120

		self.rect_3 = pygame.Rect(0, 0, self.width + 20, self.height)
		self.rect_3.y = self.rect.y + 180
		self.rect_3.x = self.screen_rect.left + 120

		self.rect_4 = pygame.Rect(0, 0, self.width + 20, self.height)
		self.rect_4.y = self.rect.y + 240
		self.rect_4.x = self.screen_rect.left + 120

		self.rect_5 = pygame.Rect(0, 0, self.width + 20, self.height)
		self.rect_5.y = self.rect.y + 300
		self.rect_5.x = self.screen_rect.left + 120

		self.prep_controls_left()
		self.prep_controls_right()
		self.prep_controls_shoot()
		self.prep_controls_quit()
		self.prep_controls_play()
		self.prep_controls_esc()



	def prep_controls_left(self):
		self.image = self.font.render("-Press left arrow key to move left ", True, self.color, self.bg_color)
		self.image_x = self.rect.x + 7
		self.image_y = self.rect.y + 2

	def prep_controls_right(self):
		self.image_ = self.font.render("-Press right arrow key to move right ", True, self.color, self.bg_color)
		self.image_x_ = self.rect.x + 7
		self.image_y_ = self.rect_1.y + 2

	def prep_controls_shoot(self):
		self.image_1 = self.font.render("-Press space to shoot ", True, self.color, self.bg_color)
		self.image_x_1 = self.rect.x + 7
		self.image_y_1 = self.rect_2.y + 2

	def prep_controls_quit(self):
		self.image_2 = self.font.render("-Press 'Q' to exit the game ", True, self.color, self.bg_color)
		self.image_x_2 = self.rect.x + 7
		self.image_y_2 = self.rect_3.y + 2

	def prep_controls_play(self):
		self.image_3 = self.font.render("-Press 'P' to play ", True, self.color, self.bg_color)
		self.image_x_3 = self.rect.x + 7
		self.image_y_3 = self.rect_4.y + 2

	def prep_controls_esc(self):
		self.image_4 = self.font.render("-Press 'ESC' to go back ", True, self.color, self.bg_color)
		self.image_x_4 = self.rect.x + 7
		self.image_y_4 = self.rect_5.y + 2



	def blit_controls(self):
		self.screen.blit(self.image, (self.image_x, self.image_y))
		self.screen.blit(self.image_, (self.image_x_, self.image_y_))
		self.screen.blit(self.image_1, (self.image_x_1, self.image_y_1))
		self.screen.blit(self.image_2, (self.image_x_2, self.image_y_2))
		self.screen.blit(self.image_3, (self.image_x_3, self.image_y_3))
		self.screen.blit(self.image_4, (self.image_x_4, self.image_y_4))


